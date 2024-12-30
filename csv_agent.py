from langchain.schema import HumanMessage, SystemMessage
import os 
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from phi.model.groq import Groq
import pandas as pd
from langchain_openai import ChatOpenAI
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_groq import ChatGroq


# Load environment variables from .env file

load_dotenv()

GROQ_API_KEY = os.getenv('GROQ_API_KEY')

llm=ChatGroq(api_key=GROQ_API_KEY, model_name="llama-3.1-70b-versatile", temperature=0.3)



# Read the csv file 
df =  pd.read_csv(r"C:\Users\khair\OneDrive\Bureau\AG_Agent_phi\AI_Agent_team\train_date.csv",
                   usecols = ["Id","L0_S0_D1","L0_S0_D3","L0_S0_D5","L0_S0_D7","L0_S0_D9","L0_S0_D11"],
                   nrows = 100, skip_blank_lines= True).fillna(0)




# Agent

agent = create_pandas_dataframe_agent(
    llm = llm,
    df = df,
    verbose=True,
    allow_dangerous_code=True,
    agent_type="tool-calling",)
    
# invoke 
res = agent.invoke("Could you provide some analysis related to quality engineering ?")

print(res)