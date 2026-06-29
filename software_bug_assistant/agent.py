from google.adk.agents.llm_agent import Agent
from tools import read_text

MODEL = 'gemini-2.5-flash'

root_agent = Agent(
    model=MODEL,
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
)

print(read_text(r"C:\Users\GNX\Desktop\test.txt"))