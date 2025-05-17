import streamlit as st
from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
from phi.tools.website import WebsiteTools
from phi.tools.crawl4ai_tools import Crawl4aiTools

load_dotenv()

# agent = Agent(tools=[WebsiteTools()], show_tool_calls=True)
# agent.print_response("Search web page: 'https://docs.phidata.com/introduction'", markdown=True)

# ## web search agent
web_search_agent=Agent(
    name="Web search Agent",
    role="Your role is to answer the user's question by searching the content from the url provided by the user.",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[Crawl4aiTools(max_length=None)],
    instructions=["Always include sources"],
    show_tools_calls=True,
    markdown=True,
)

def response(url, prompt):
    return web_search_agent.run(f"{prompt}, url of the web page is {url}").content

web_search_agent.print_response("list all the content from this page https://docs.phidata.com/tools/crawl4ai", markdown=True)