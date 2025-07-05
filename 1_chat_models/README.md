# Chat Models

This directory contains examples of chat models using LangChain.

## Examples

- [1_chat_model_basic.py](1_chat_model_basic.py): A basic chat model example.
- [2_chat_model_basic_conversation.py](2_chat_model_basic_conversation.py): A basic chat model example with conversation.
- [3_chat_model_alternatives.py](3_chat_model_alternatives.py): A basic chat model example with conversation.
- [4_chat_model_conversation_with_user.py](4_chat_model_conversation_with_user.py): A basic chat model example with conversation.
- [5_chat_model_save_message_history_firebase.py](5_chat_model_save_message_history_firebase.py): A basic chat model example with conversation.

## How to run

```bash
python 1_chat_models/1_chat_model_basic.py
```

```bash
python 1_chat_models/2_chat_model_basic_conversation.py
```

```bash
python 1_chat_models/3_chat_model_alternatives.py
```

```bash
python 1_chat_models/4_chat_model_conversation_with_user.py
```

```bash
python 1_chat_models/5_chat_model_save_message_history_firebase.py
```

## Output

```bash
Full result:

Content only:
```
# Tutorial Description

## 1. Basic Chat Model
- Introduction to LangChain's chat models
- Simple message passing
- Basic model configuration

## 2. Basic Conversation
- Multi-turn conversations
- Message history management
- Context preservation

## 3. Alternative Models
- Working with different LLM providers
- Model comparison
- Configuration options

## 4. Interactive Chat
- User input handling
- Real-time conversation flow
- Error handling

## 5. Message History with Firebase
- Persistent message storage
- Firebase integration
- Retrieving conversation history

## 🔧 Dependencies

- langchain: Core LangChain functionality
- langchain-google-genai: Google Gemini integration
- python-dotenv: Environment variable management
- firebase-admin: Firebase integration (for message history)
