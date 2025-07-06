# Code Details: Agents and Tools Implementation

This document provides a detailed explanation of each file in the `agent_deep_dive` and `tools_deep_dive` directories.

## Table of Contents
1. [Agent Deep Dive](#agent-deep-dive)
   - [1_agent_react_chat.py](#1_agent_react_chatpy)
   - [2_agent_react_docstore.py](#2_agent_react_docstorepy)
2. [Tools Deep Dive](#tools-deep-dive)
   - [1_tool_constructor.py](#1_tool_constructorpy)
   - [2_tool_decorator.py](#2_tool_decoratorpy)
   - [3_tool_base_tool.py](#3_tool_base_toolpy)

---

## Agent Deep Dive

### 1_agent_react_chat.py
Implements a ReAct (Reasoning and Acting) agent with chat capabilities.

**Key Components:**
- Uses `ChatGoogleGenerativeAI` for the language model
- Implements a simple chat interface
- Demonstrates basic agent interaction

**Main Functions:**
- `main()`: Sets up the agent and handles the chat loop
- `process_input()`: Processes user input and gets agent's response

**Dependencies:**
- langchain_google_genai
- python-dotenv

---

### 2_agent_react_docstore.py
Demonstrates using a ReAct agent with a document store.

**Key Components:**
- Implements document search and retrieval
- Uses ChromaDB for document storage
- Shows how to customize agent prompts

**Main Classes:**
- `DocumentSearchTool`: Custom tool for searching documents

**Dependencies:**
- langchain_chroma
- langchain_text_splitters

---

## Tools Deep Dive

### 1_tool_constructor.py
Shows how to create tools using the constructor pattern.

**Key Features:**
- Creates tools using `Tool.from_function()`
- Demonstrates simple tool implementation
- Shows how to handle tool inputs and outputs

**Example Tools:**
- Search tool
- Calculator tool

**Dependencies:**
- langchain.tools

---

### 2_tool_decorator.py
Demonstrates creating tools using the `@tool` decorator.

**Key Features:**
- Uses `@tool` decorator for quick tool creation
- Shows how to add docstrings for tool descriptions
- Implements error handling in tools

**Example Tools:**
- Web search tool
- File operation tool

**Dependencies:**
- langchain.tools

---

### 3_tool_base_tool.py
Implements custom tools by subclassing `BaseTool`.

**Key Features:**
- Full control over tool behavior
- Custom input validation
- Advanced error handling

**Main Classes:**
- [SimpleSearchTool](cci:2://file:///Users/praveenkumar/Desktop/Studies/langchain-tutorial/5_agents_and_tools/tools_deep_dive/3_tool_base_tool.py:9:0-21:45): Searches using Tavily API
- [MultiplyNumbersTool](cci:2://file:///Users/praveenkumar/Desktop/Studies/langchain-tutorial/5_agents_and_tools/tools_deep_dive/3_tool_base_tool.py:52:0-64:56): Performs multiplication

**Dependencies:**
- tavily-python
- pydantic

---

## Common Patterns

### Tool Creation
1. **Constructor Pattern**: Best for simple tools
   ```python
   from langchain.tools import Tool
   tool = Tool.from_function(func=my_function, name="my_tool")

2. **Decorator Pattern**: Clean syntax for function-based tools
    ```python
from langchain.tools import tool
@tool
def my_tool(query: str) -> str:
    """Tool description here."""
    return "Result"
```

3. **BaseTool Subclass**: For complex tools needing full control
   ```python
from langchain.tools import BaseTool
class MyTool(BaseTool):
    name = "my_tool"
    description = "Tool description"
    def _run(self, query: str) -> str:
        return "Result"
```

**Error Handling**
- Always validate inputs
- Use try-catch blocks for external API calls
- Provide meaningful error messages

**Best Practices**
- Keep tool functions focused on a single task
- Document tool purpose, inputs, and outputs
- Handle edge cases gracefully
- Use type hints for better code clarity
