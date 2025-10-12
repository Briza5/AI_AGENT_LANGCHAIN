from dotenv import load_dotenv  # Import the load_dotenv function to load environment variables from a .env file
import os # Import the os module to access environment variables

from langchain_core.messages import (AIMessage, HumanMessage, SystemMessage)  # Import message classes from langchain_core.messages
from langchain_core.output_parsers import StrOutputParser  # Import StrOutputParser from langchain_core.output_parsers
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder  # Import ChatPromptTemplate from langchain_core.prompts
from langchain_google_genai import ChatGoogleGenerativeAI  # Import ChatGoogleGenerativeAI from langchain_google_genai
from langchain.tools import tool  # Import the tool decorator from langchain.tools
from langchain.agents import create_openai_tools_agent, AgentExecutor  # Import create_openai_tools_agent from langchain.agents

load_dotenv()  # Load environment variables from .env file

todoist_api_token = os.getenv("TODOIST_API_TOKEN")  # Get the API token from environment variables
gemini_api_key = os.getenv("GEMINI_API_KEY") # Get the Gemini API key from environment variables

@tool
def add_task(task):
    """Přidá úkol do uživatelského task listu. Použij pokud uživatel chce přidat nebo vytvořit nový úkol."""  # Tool description in Czech
    print(task)  # Function to simulate adding a task to Todoist
    print("Úkol přidán!")  # Print confirmation message


tools = [add_task]  # List of tools available for the model
# Initialize the ChatGoogleGenerativeAI model with the specified parameters
llm = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash',
    google_api_key=gemini_api_key,
    temperature=0.3)

system_prompt = "Jseš nápomocný asistent, který pomáhá uživatelům přidávat úkoly do Todoist."  # Define the system prompt in Czech
user_input = "Přidej nový úkol ať koupím mléko."  # Define the user input in Czech

# Define the prompt template with system and human messages
prompt = ChatPromptTemplate([
    ("system", system_prompt),
    ("user", user_input),
    MessagesPlaceholder("agent_scratchpad")
    ])

#chain = prompt | llm | StrOutputParser()  # Create a chain that processes the prompt through the LLM and parses the output
agent = create_openai_tools_agent(llm, tools, prompt=prompt)  # Create an agent with the LLM, tools, and prompt
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=False)  # Create an AgentExecutor to manage the agent's execution

#response = chain.invoke({"input": user_input})  # Invoke the chain with the user input
response = agent_executor.invoke({"input": user_input})  # Invoke the agent executor with the user input
print(response)  # Print the response from the model