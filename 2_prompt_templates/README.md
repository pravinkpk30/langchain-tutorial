# Prompt Templates in LangChain

This directory contains examples of using LangChain's `PromptTemplate` and `ChatPromptTemplate` classes to create reusable prompts for language models.

## Why Use Prompt Templates?

Prompt templates help you:
- Standardize prompt formats across your application
- Dynamically insert variables into prompts
- Maintain consistent prompt structures
- Make your code more maintainable and reusable

## Files Overview

### 1. [1_prompt_template_basic.py](cci:7://file:///Users/praveenkumar/Desktop/Studies/langchain-tutorial/2_prompt_templates/1_prompt_template_basic.py:0:0-0:0)

**Purpose**: Demonstrates basic usage of `PromptTemplate` with a simple text completion model.

**Key Concepts:**
- Creating a basic prompt template
- Formatting prompts with variables
- Using different template formats

**Example Usage:**
```python
from langchain.prompts import PromptTemplate

# Simple prompt with one input variable
template = "Tell me a {adjective} joke about {content}."
prompt = PromptTemplate.from_template(template)

# Format the prompt
formatted_prompt = prompt.format(adjective="funny", content="chickens")
print(formatted_prompt)
```

### 2. [2_prompt_template_with_chat_model.py](cci:7://file:///Users/praveenkumar/Desktop/Studies/langchain-tutorial/2_prompt_templates/2_prompt_template_with_chat_model.py:0:0-0:0)

**Purpose**: Shows how to use `ChatPromptTemplate` with chat models, including system messages and multiple message types.

**Key Concepts:**
- Working with chat models
- Creating chat prompt templates
- Using system and human messages
- Multiple placeholders in templates

**Code Breakdown:**

# Part 1: Basic chat prompt template
template = "Tell me a joke about {topic}."
prompt_template = ChatPromptTemplate.from_template(template)

# Part 2: Multiple placeholders
template_multiple = """You are a helpful assistant.
Human: Tell me a {adjective} short story about a {animal}."""
prompt_multiple = ChatPromptTemplate.from_template(template_multiple)

# Part 3: System and human messages
messages = [
    ("system", "You are a comedian who tells jokes about {topic}."),
    ("human", "Tell me {joke_count} jokes."),
]
prompt_template = ChatPromptTemplate.from_messages(messages)

# Invoke the model with a message
result = model.invoke(prompt_template.invoke({"topic": "cats", "joke_count": 3}))
print(result.content)
```

**How to run:**
```bash
python 2_prompt_templates/2_prompt_template_with_chat_model.py
```

**Output:**
```bash

```

# Best Practices

- Use `ChatPromptTemplate` for chat models
- Use `PromptTemplate` for text completion models
- Use `ChatPromptTemplate.from_messages` for system and human messages
- Use `PromptTemplate.from_template` for simple templates

- Keep templates maintainable: Store templates in separate files or constants
- Use descriptive variable names: Makes templates more readable
- Handle missing variables: Always provide defaults or handle missing variables
- Version your templates: Helps track changes over time
- Test different templates: Experiment with different phrasings and structures

# 🔧 Dependencies

- langchain: Core LangChain functionality
- langchain-google-genai: Google Gemini integration
- python-dotenv: Environment variable management
