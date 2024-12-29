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

# Set your API key

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("The GROQ_API_KEY environment variable is not set")

# Initialize Groq model with API key
groq_model = Groq(id="llama3-groq-70b-8192-tool-use-preview", api_key=GROQ_API_KEY)

# Agent 1
web_agent = Agent(
    name="Web Agent",
    role="Generate a quality Engineering Datasets, better to be csv files format",
    model=groq_model,
    tools=[DuckDuckGo()],
    instructions=["Not necessarly includes sources"],
    show_tool_calls=True,
    markdown=True,
)

# Agent 2
data_analyst = DuckDbAgent(
    model=groq_model,
    semantic_model=json.dumps(
        {
            "tables": [
                {
                    "name": "Quality Engineering Analysis table",
                    "description": "Contains information about Product Quality.",
                    "path": "https://www.kaggle.com/competitions/bosch-production-line-performance/data?select=train_numeric.csv.zip",
                }
            ]
        }
    ),
    markdown=True,
)

# Agent 3 (Team)
agent_team = Agent(
    team=[web_agent, data_analyst],
    model=groq_model,
    instructions=[ "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

agent_team.print_response("Summarize and Do Data Analysis related to Quality Engineering and interpret the results obtained: Specifically CPK,CP, ANOVA test if needed ", stream=True)
