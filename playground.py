from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.playground import Playground, serve_playground_app
from agno.storage.agent.sqlite import SqliteAgentStorage
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
from agno.models.groq import Groq

import os
from dotenv import load_dotenv
load_dotenv()

# Load environment variables
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
# Uncomment if using OpenAI models
#os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

agent_storage: str = "tmp/agents.db"

# News Sentiment Agent
news_sentiment_agent = Agent(
    name="News Sentiment Agent",
    model=Groq(id="qwen-2.5-32b"),
    description="You are a News Sentiment Decoding Assistant. Decode the news and provide the sentiment ranging from +10 to -10 in table format with the following columns Date, Time, News, Source and Score. Also provide reasoning explanation point by point after the Table",
    tools=[DuckDuckGoTools(fixed_max_results=10)],
    storage=SqliteAgentStorage(table_name="news_sentiment_agent", db_file=agent_storage),
    add_datetime_to_instructions=True,
    add_history_to_messages=True,
    num_history_responses=5,
    markdown=True,
)

# Finance Agent
finance_agent = Agent(
    name="Finance Agent",
    model=Groq(id="qwen-2.5-32b"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=["Always use tables to display data. If the stock is related to Indian Stock use .NS to the symbol for example if the stock symbol is SBIN then add SBIN.NS to it"],
    storage=SqliteAgentStorage(table_name="finance_agent", db_file=agent_storage),
    add_datetime_to_instructions=True,
    add_history_to_messages=True,
    num_history_responses=5,
    markdown=True,
)

# Web Agent (keeping this from your original playground)
web_agent = Agent(
    name="Web Agent",
    model=Groq(id="qwen-2.5-32b"),
    tools=[DuckDuckGoTools()],
    instructions=["Always include sources"],
    storage=SqliteAgentStorage(table_name="web_agent", db_file=agent_storage),
    add_datetime_to_instructions=True,
    add_history_to_messages=True,
    num_history_responses=5,
    markdown=True,
)

# Combined Agent - integrates both news sentiment and stock price functionality
combined_agent = Agent(
    name="Financial News & Stock Agent",
    model=Groq(id="llama3-70b-8192"),  # Using GPT-4o for better reasoning with combined tasks
    tools=[DuckDuckGoTools(), YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=[
        "You are a Financial News and Stock Analysis Assistant.",
        "For news queries, decode the news sentiment ranging from +10 to -10 in table format with columns: Date, Time, News, Source and Score.",
        "Include the current stock price, key metrics, and recent price movement when a company is mentioned.",
        "Always provide reasoning for sentiment scores point by point after the tables.",
        "Always present financial data in tables for clarity.",
        "Always use tables to display data. If the stock is related to Indian Stock use .NS to the symbol for example if the stock symbol is SBIN then add SBIN.NS to it"
    ],
    storage=SqliteAgentStorage(table_name="combined_agent", db_file=agent_storage),
    add_datetime_to_instructions=True,
    add_history_to_messages=True,
    num_history_responses=5,
    markdown=True,
)

# Setting up the playground with all agents
app = Playground(agents=[combined_agent, news_sentiment_agent, finance_agent, web_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)


