from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from phi.model.groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()

# Set your API key as an environment variable
# Example: export GROQ_API_KEY="your_api_key"
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("The GROQ_API_KEY environment variable is not set")

# Initialize Groq model with API key
groq_model = Groq(id="llama3-groq-70b-8192-tool-use-preview", api_key=GROQ_API_KEY)

# Agent 1
web_agent = Agent(
    name="Web Agent",
    role="Search the web for information quality Engineering Datasets, better to be csv files format",
    model=groq_model,
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

# Agent 2
finance_agent = Agent(
    name="Quality Engineering Agent",
    role="Get Quality Engineering data to do CPK, PK, and ANOVA is possible",
    model=groq_model,
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
    instructions=["Use tables to display data, python pandas DataFrames if possible"],
    show_tool_calls=True,
    markdown=True,
)

# Agent 3 (Team)
agent_team = Agent(
    team=[web_agent, finance_agent],
    model=groq_model,
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

agent_team.print_response("Summarize and Do Data Analysis related to Quality Engineering and interpret the results obtained: Specifically CPK,CP, ANOVA test if needed for any company in your choice", stream=True)
