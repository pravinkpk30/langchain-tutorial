# LangChain Tutorial

A comprehensive tutorial series for learning LangChain, covering various aspects of building applications with language models.

## 🚀 Features

- Step-by-step tutorials on LangChain fundamentals
- Practical examples of chat models
- Integration with various LLM providers
- Hands-on exercises and code samples
- Best practices for production applications

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8+
- pip (Python package manager)
- Git (for version control)
- Google Cloud account (for Google Gemini API access)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone [https://github.com/yourusername/langchain-tutorial.git](https://github.com/yourusername/langchain-tutorial.git)
   cd langchain-tutorial
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file** in the `langchain-tutorial` directory with your API key:
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   ```

5. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```

6. **Run the tutorial**
   ```bash
   python 1_chat_models/1_chat_model_basic.py
   ```

