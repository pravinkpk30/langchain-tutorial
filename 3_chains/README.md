# LangChain Chains

This directory contains examples demonstrating different types of chains in LangChain, from basic to advanced usage.

## 🧩 What are Chains in LangChain?

Chains allow you to combine multiple components (like models, prompts, and other chains) into a single, callable unit. They are the building blocks of complex LLM applications.

## 📚 Files Overview

### 1. [1_chains_basics.py](cci:7://file:///Users/praveenkumar/Desktop/Studies/langchain-tutorial/3_chains/1_chains_basics.py:0:0-0:0)
**Purpose**: Introduction to basic chain usage in LangChain.

**Key Concepts:**
- `LLMChain`: The most basic type of chain
- Simple prompt chaining
- Basic input/output handling

**Example:**
```python
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
    input_variables=["topic"],
    template="Tell me a joke about {topic}."
)
chain = LLMChain(llm=model, prompt=prompt)
response = chain.run("lawyers")

### 2. [2_chains_under_the_hood_runnable.py](cci:7://file:///Users/praveenkumar/Desktop/Studies/langchain-tutorial/3_chains/2_chains_under_the_hood_runnable.py:0:0-0:0)
**Purpose**: Demonstrates the underlying Runnable interface that powers LangChain.

**Key Concepts:**
- RunnableLambda: Wraps Python functions as runnable steps
- RunnableSequence: Chains multiple runnables together
- Custom chain composition

**Example:**
```python
format_prompt = RunnableLambda(lambda x: prompt_template.format_prompt(**x))
invoke_model = RunnableLambda(lambda x: model.invoke(x.to_messages()))
parse_output = RunnableLambda(lambda x: x.content)

chain = RunnableSequence(
    first=format_prompt,
    middle=[invoke_model],
    last=parse_output
)
response = chain.invoke({"topic": "lawyers"})
print(response)
```

### 3. [3_chains_extended.py](cci:7://file:///Users/praveenkumar/Desktop/Studies/langchain-tutorial/3_chains/3_chains_extended.py:0:0-0:0)
**Purpose**: Shows extended chain functionality with more complex operations.

**Key Concepts:**
- Multiple input/output handling
- Chaining multiple operations
- Error handling in chains

**Example:**
```python
from langchain.schema.runnable import RunnablePassthrough

chain = (
    {"topic": RunnablePassthrough()}
    | prompt_template
    | model
    | output_parser
)
response = chain.invoke({"topic": "lawyers"})
print(response)
``` 

### 4. [4_chains_parallel.py](cci:7://file:///Users/praveenkumar/Desktop/Studies/langchain-tutorial/3_chains/4_chains_parallel.py:0:0-0:0)
**Purpose**: Demonstrates parallel execution of chains in LangChain.

**Key Concepts:**
- Parallel execution of chains
- Branching in chains
- Combining results from multiple chains
- RunnableParallel: Runs multiple runnables in parallel
- Combining multiple chains
- Aggregating results

**Example:**
```python
from langchain.schema.runnable import RunnablePassthrough

chain = (
    {"topic": RunnablePassthrough()}
    | prompt_template
    | model
    | output_parser
)
response = chain.invoke({"topic": "lawyers"})
print(response)
```
```python
from langchain.schema.runnable import RunnableParallel

chain = RunnableParallel(
    joke=chain1,
    translation=chain2
)

result = chain.invoke({"input": "chickens"})
print(result)
```

### 5. [5_chains_branching.py](cci:7://file:///Users/praveenkumar/Desktop/Studies/langchain-tutorial/3_chains/5_chains_branching.py:0:0-0:0)
**Purpose**: Shows conditional logic and branching in chains.

**Key Concepts:**
- Branching in chains
- Conditional logic
- RunnableBranch: Branches based on conditions
- RunnableBranch: Implements if/else logic
- Conditional routing
- Dynamic chain selection

**Example:**
```python
from langchain.schema.runnable import RunnableBranch

branch = RunnableBranch(
    (lambda x: "positive" in x["sentiment"].lower(), positive_chain),
    (lambda x: "negative" in x["sentiment"].lower(), negative_chain),
    neutral_chain
)
```
## Core Concepts
### RunnableLambda
Wraps a Python function into a runnable step in the chain.

### Use When:
- You need custom processing
- Converting between different data formats
- Simple transformations

### Example:
```python
add_one = RunnableLambda(lambda x: x + 1)
```
### RunnableParallel
Runs multiple runnables in parallel and combines their outputs.

### Use When:
- You need to execute multiple chains simultaneously
- Combining outputs from different sources
- Fan-out/fan-in patterns

### Example:
```python
chain = RunnableParallel(
    joke=chain1,
    translation=chain2
)
```
### RunnableBranch
Implements conditional logic to route inputs to different chains.

### Use When:
- You need if/else logic in your chain
- Dynamic chain selection
- Content-based routing

### Example:
```python
branch = RunnableBranch(
    (lambda x: x["value"] > 0, positive_chain),
    negative_chain
)
```
### 🛠️ Best Practices
- Keep Chains Focused: Each chain should do one thing well
- Use Composition: Build complex chains from simple ones
- Handle Errors: Implement proper error handling
- Logging: Add logging for debugging
- Testing: Test each chain component independently



