from google.adk import Agent
from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
import os

hotel_agent = Agent(
    name="hotel_agent",
    model="gemini-2.0-flash-exp",
    description="Finds hotels within the destination and budget for the given travel dates.",
    instruction="""
                  You are a hotel booking agent. The coordinator will give you:
                  - destination
                  - start_date
                  - end_date
                  - budget_amount
                  - budget_currency
                  
                  Return 1-2 mock hotel suggestions including:
                  - Hotel name
                  - Nightly rate and total cost in the given currency
                  - Main features
                  
                  Ensure the total price fits the budget.
                 """
)

# https://google.github.io/adk-docs/agents/models/#using-cloud-proprietary-models-via-litellm

# This works
hotel_agent_openai = LlmAgent(
    name="hotel_agent",
    model=LiteLlm(model="openai/gpt-4o"),
    description="Finds hotels within the destination and budget for the given travel dates.",
    instruction="""
                  You are a hotel booking agent. The coordinator will give you:
                  - destination
                  - start_date
                  - end_date
                  - budget_amount
                  - budget_currency
                  
                  Return 1-2 mock hotel suggestions including:
                  - Hotel name
                  - Nightly rate and total cost in the given currency
                  - Main features
                  
                  Ensure the total price fits the budget.
                 """
)

# https://github.com/google/adk-python/issues/49
# LiteLlm issue with Ollama
os.environ["OPENAI_API_BASE"] = os.getenv("OPENAI_BASE_URL")

model = os.getenv("CHAT_MODEL", "gpt-4o-mini")

AGENT_MODEL = "ollama_chat/mistral-small3.1" # works
hotel_agent_ollama = Agent(
    name="hotel_agent",
    model=LiteLlm(model="openai/" + model),
    description="Finds hotels within the destination and budget for the given travel dates.",
    instruction="""
                  You are a hotel booking agent. The coordinator will give you:
                  - destination
                  - start_date
                  - end_date
                  - budget_amount
                  - budget_currency
                  
                  Return 1-2 mock hotel suggestions including:
                  - Hotel name
                  - Nightly rate and total cost in the given currency
                  - Main features
                  
                  Ensure the total price fits the budget.
                 """
)



