from google.adk.agents.llm_agent import LlmAgent
from .tools import search_tool, github_mcp_tools, read_text, write_text, list_directory, run_command

MODEL = 'gemini-2.5-flash'



root_agent = LlmAgent(
    model=MODEL,
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
)
