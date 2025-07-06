# LangChain Agents & Tools Tutorial

This directory contains examples and tutorials for working with LangChain's agents and tools. It's organized into two main sections: `agent_deep_dive` and `tools_deep_dive`.

## Prerequisites

1. Python 3.8+
2. Required packages (install using `pip install -r requirements.txt`):
   - langchain_google_genai
   - dotenv
   - langchain_community
   - firecrawl-py
   - langchain_chroma
   - langchain_huggingface
   - wikipedia
   - pydantic
   - tavily-python

3. API Keys:
   - Create a `.env` file in the root directory with your API keys:
     ```
     GOOGLE_API_KEY=your_google_api_key
     TAVILY_API_KEY=your_tavily_api_key
     ```

## Directory Structure

### 1. agent_deep_dive

This directory contains examples of building and working with LangChain agents.

#### Files:
- [1_agent_react_chat.py](cci:7://file:///Users/praveenkumar/Desktop/Studies/langchain-tutorial/5_agents_and_tools/agent_deep_dive/1_agent_react_chat.py:0:0-0:0): Implements a ReAct (Reasoning and Acting) agent with chat capabilities.
- [2_agent_react_docstore.py](cci:7://file:///Users/praveenkumar/Desktop/Studies/langchain-tutorial/5_agents_and_tools/agent_deep_dive/2_agent_react_docstore.py:0:0-0:0): Demonstrates using a ReAct agent with a document store.

#### How to run:
```bash
# Run the chat agent
python agent_deep_dive/1_agent_react_chat.py

# Run the document store agent
python agent_deep_dive/2_agent_react_docstore.py
```

### 2. tools_deep_dive
This directory demonstrates different ways to create and use tools with LangChain.

#### Files:
- [1_tool_constructor.py](cci:7://file:///Users/praveenkumar/Desktop/Studies/langchain-tutorial/5_agents_and_tools/tools_deep_dive/1_tool_constructor.py:0:0-0:0): Shows how to create tools using the constructor pattern.
- [2_tool_decorator.py](cci:7://file:///Users/praveenkumar/Desktop/Studies/langchain-tutorial/5_agents_and_tools/tools_deep_dive/2_tool_decorator.py:0:0-0:0): Demonstrates creating tools using the @tool decorator.
- [3_tool_base_tool.py](cci:7://file:///Users/praveenkumar/Desktop/Studies/langchain-tutorial/5_agents_and_tools/tools_deep_dive/3_tool_base_tool.py:0:0-0:0): Implements custom tools by subclassing BaseTool.

#### How to run:
```bash
# Run the tool constructor example
python tools_deep_dive/1_tool_constructor.py

# Run the decorator example
python tools_deep_dive/2_tool_decorator.py

# Run the BaseTool example
python tools_deep_dive/3_tool_base_tool.py
```

### Key Concepts

#### Agents
- ReAct Agent: Implements the ReAct (Reasoning and Acting) framework for agents.
- Document Store Agent: Shows how to work with document stores in agents.

#### Tools
- Constructor Pattern: Creating tools using the Tool constructor.
- Decorator Pattern: Using the @tool decorator for quick tool creation.
- BaseTool Class: Creating custom tools by subclassing BaseTool for more control.

### Common Issues & Solutions
#### Missing API Keys:
- Ensure you have a .env file with the required API keys.
- Make sure the .env file is in the root directory.

#### Package Not Found:
- Run pip install -r requirements.txt to install all dependencies.
- If using a virtual environment, make sure it's activated.

#### Tavily API Errors:
- Verify your Tavily API key is correct.
- Check your internet connection.

### Additional Resources
- LangChain Documentation
- Tavily API Documentation
- Google Generative AI
