from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai


#web serach agent
web_search_agent=Agent(
    name="Web Search Agent",
    role="Search the Web for the information",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls= True,
    markdown=True,
)

#financial agent
Finance_search_agent=Agent(
    name="Finance Ai Agent",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,company_news=True)
    ],
    instructions=["Use tables to display the data "],
    show_tools_calls=True,
    markdown= True,
)

#multimodel -agent 

multi_ai_agent = Agent(
    team=[web_search_agent,Finance_search_agent],
    instructions=["always iclude sources", "use table to display the data"],
    show_tool_calls= True,
    markdown= True, 
)

multi_ai_agent.print_response("summarize analyst recommendation and share the latest news for NVDA", stream = True)
