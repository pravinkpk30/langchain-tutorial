from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
import os

# Load environment variables from .env
load_dotenv()

# Create a ChatOpenAI model
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", api_key=os.getenv("GOOGLE_API_KEY"))


chat_history = []  # Use a list to store messages

# Set an initial system message (optional)
system_message = SystemMessage(content="You are a helpful AI assistant.")
chat_history.append(system_message)  # Add system message to chat history

# Chat loop
while True:
    query = input("You: ")
    if query.lower() == "exit":
        break
    chat_history.append(HumanMessage(content=query))  # Add user message

    # Get AI response using history
    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response))  # Add AI message

    print(f"AI: {response}")


print("---- Message History ----")
print(chat_history)