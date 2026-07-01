from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools import google_search, AgentTool
from google.adk.tools.mcp_tool import McpToolset, StreamableHTTPConnectionParams
import os

search_agent = LlmAgent(
    name='search_agent',
    model='gemini-2.5-flash',
    description="A search agent",
    instruction="You are an expert at Google Search.. Your job is to perform a search to solve the problem",
    tools=[google_search]
)

github_mcp_tools = McpToolset(
    connection_params=StreamableHTTPConnectionParams(
        url='https://api.githubcopilot.com/mcp',
        headers={
            "Authorization": f"Bearer {os.getenv('GITHUB_ACCESS_TOKEN')}",
            "X-MCP-Readonly": "True"
        }
    )
)

search_tool = AgentTool(search_agent)