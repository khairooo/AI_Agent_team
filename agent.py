from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from phi.model.groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()
from phi.agent.duckdb import DuckDbAgent
import json
from phi.model.ollama import Ollama
import pandas as pd 
import dask.dataframe as dd
from phi.file.local.csv import CsvFile
from phi.agent.python import PythonAgent
from pathlib import Path 


# When creating your agent, you can enable the dangerous code execution as follows:





# Set your API key

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("The GROQ_API_KEY environment variable is not set")

# Initialize Groq model with API key
groq_model = Groq(id="llama3-groq-70b-8192-tool-use-preview", api_key=GROQ_API_KEY)
ollama_model=Ollama(id="llama3.1")


# Data: 
cwd = Path(__file__).parent.resolve()
tmp = cwd.joinpath("tmp")
if not tmp.exists():
    tmp.mkdir(exist_ok= True,parents=True)
#path to the local data:
data = "train_date.csv"

# Ensure that the data exists in the local data directory:

if not os.path.exists(data):
    raise FileNotFoundError(f"The file {data} does not exist.")
#  
# PythonAgent with Groq 
python_agent = PythonAgent(
    model =  groq_model,
    base_dir = tmp,
    files= [
        CsvFile(
            path = data ,
            description="A CSV file containing Quality Engineering Datasets",
            format="csv",
        )
    ],
    markdown = True, 
)

# # Agent 1
# web_agent = Agent(
#     description= "A Agent to help extract information about Quality Engineering",
#     name="Web Agent",
#     role="Generate a quality Engineering Datasets, better to be csv files format",
#     model=groq_model,
#     tools=[DuckDuckGo()],
#     instructions=["Not necessarly includes sources"],
#     show_tool_calls=True,
#     markdown=True,
# )

# Agent 2
data_analyst = DuckDbAgent(
    model=ollama_model,
    tools = [DuckDuckGo()],
    semantic_model=json.dumps(
        {
            "tables": [
                {
                    "name": "Quality Engineering Analysis table",
                    "description": "A Dataset from Kaggle contains informations about production line.",
                    "path": data,
                }
            ]
        }
    ),
    markdown=True,
)

# Agent 3 (Team)
agent_team = Agent(
    team=[data_analyst, python_agent],
    model=groq_model,
    instructions=[ "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

agent_team.print_response("Analysis the Data And provide some statistics ", stream=True)
