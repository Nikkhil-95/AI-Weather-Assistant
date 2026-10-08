# ============================================================
# AI Weather Chatbot with Live Weather Tool
# ============================================================

# -------------------------
# Imports
# -------------------------

from rich import print
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.messages import (
    HumanMessage,
    ToolMessage
)
from langchain_community.utilities import OpenWeatherMapAPIWrapper
from langchain.tools import tool


# -------------------------
# Load Environment Variables
# -------------------------

load_dotenv()


# -------------------------
# Initialize Weather API
# -------------------------

weather = OpenWeatherMapAPIWrapper()


# -------------------------
# Initialize LLM
# -------------------------

llm = ChatGroq(
    model="openai/gpt-oss-20b"
)


# -------------------------
# Define Weather Tool
# -------------------------

@tool
def get_weather(location: str) -> str:
    """
    Get the current weather for a given location.
    """
    return weather.run(location)


# -------------------------
# Bind Tool to LLM
# -------------------------

llm_with_tool = llm.bind_tools([get_weather])


# -------------------------
# Chat History
# -------------------------

chat_history = []


# -------------------------
# Chatbot Introduction
# -------------------------

print("🌤️ Welcome to the AI Weather Assistant!") 
print("Ask me for the current weather in any location.") 
print("Type 'exit' to end the chat.")

# -------------------------
# Main Chat Loop
# -------------------------

while True:

    # Get user input
    user_query = input("User: ")

    # Exit the chatbot
    if user_query.lower() == "exit":
        break

    # Add user message to chat history
    chat_history.append(
        HumanMessage(content=user_query)
    )

    # Send conversation to LLM
    response = llm_with_tool.invoke(chat_history)

    # Store LLM response in chat history
    chat_history.append(response)

    # -------------------------
    # Handle Tool Calls
    # -------------------------

    if response.tool_calls:

        for tool_call in response.tool_calls:

            # Check if the requested tool is get_weather
            if tool_call["name"] == "get_weather":
                result = get_weather.invoke(
                    tool_call["args"]
                )

            # Create a ToolMessage with the tool result
            tool_message = ToolMessage(
                content=result,
                tool_call_id=tool_call["id"]
            )

            # Add tool result to chat history
            chat_history.append(tool_message)

    # -------------------------
    # Generate Final Response
    # -------------------------

    final_response = llm_with_tool.invoke(chat_history)

    # Store final response in chat history
    chat_history.append(final_response)

    # Display AI response
    print(f"AI: {final_response.content}")
