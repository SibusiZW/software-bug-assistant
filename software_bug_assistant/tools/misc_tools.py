from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools import google_search, AgentTool

search_agent = LlmAgent(
    name='search_agent',
    model='gemini-2.5-flash',
    description="A search agent",
    instruction="You are an expert at Google Search.. Your job is to perform a search to solve the problem",
    tools=[google_search]
)

search_tool = AgentTool(search_agent)