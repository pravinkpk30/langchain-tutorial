# RAG with LangChain

This directory contains examples of Retrieval-Augmented Generation (RAG) implementations using LangChain, covering various aspects from basic setup to advanced features.

## 🏗️ Project Structure

- `books/`: Contains sample text files for testing RAG functionality.
- `db/`: Directory for storing vector stores and embeddings.
- `rag_basic.py`: Basic RAG implementation using LangChain.
- `rag_conversational.py`: Conversational RAG implementation using LangChain.
- `rag_web_scrape_basic.py`: Basic web scraping and RAG implementation using LangChain.
- `rag_web_scrape_firecrawl.py`: Web scraping and RAG implementation using LangChain and FireCrawl.

## 📚 Files Overview

- `rag_basic.py`: Basic RAG implementation using LangChain.
- `rag_conversational.py`: Conversational RAG implementation using LangChain.
- `rag_web_scrape_basic.py`: Basic web scraping and RAG implementation using LangChain.
- `rag_web_scrape_firecrawl.py`: Web scraping and RAG implementation using LangChain and FireCrawl.


## 📚 File Descriptions

### 1. Basic RAG Implementation
- **[1a_rag_basics.py](cci:7://file:///Users/praveenkumar/Desktop/Studies/langchain-tutorial/4_rag/1a_rag_basics.py:0:0-0:0)**: Basic RAG pipeline with ChromaDB and HuggingFace embeddings
- **[1b_rag_basics.py](cci:7://file:///Users/praveenkumar/Desktop/Studies/langchain-tutorial/4_rag/1b_rag_basics.py:0:0-0:0)**: Enhanced version with better error handling and logging

### 2. Metadata Handling
- **[2a_rag_basics_metadata.py](cci:7://file:///Users/praveenkumar/Desktop/Studies/langchain-tutorial/4_rag/2a_rag_basics_metadata.py:0:0-0:0)**: Basic metadata usage in RAG
- **[2b_rag_basics_metadata.py](cci:7://file:///Users/praveenkumar/Desktop/Studies/langchain-tutorial/4_rag/2b_rag_basics_metadata.py:0:0-0:0)**: Advanced metadata filtering and querying

### 3. Core Components
- **[3_rag_text_splitting_deep_dive.py](cci:7://file:///Users/praveenkumar/Desktop/Studies/langchain-tutorial/4_rag/3_rag_text_splitting_deep_dive.py:0:0-0:0)**: Different text splitting strategies
- **[4_rag_embedding_deep_dive.py](cci:7://file:///Users/praveenkumar/Desktop/Studies/langchain-tutorial/4_rag/4_rag_embedding_deep_dive.py:0:0-0:0)**: Comparison of embedding models
- **[5_rag_retriever_deep_dive.py](cci:7://file:///Users/praveenkumar/Desktop/Studies/langchain-tutorial/4_rag/5_rag_retriever_deep_dive.py:0:0-0:0)**: Various retriever types and configurations

### 4. Application Examples
- **[6_rag_one_off_question.py](cci:7://file:///Users/praveenkumar/Desktop/Studies/langchain-tutorial/4_rag/6_rag_one_off_question.py:0:0-0:0)**: Single question-answering
- **[7_rag_conversational.py](cci:7://file:///Users/praveenkumar/Desktop/Studies/langchain-tutorial/4_rag/7_rag_conversational.py:0:0-0:0)**: Conversational RAG with memory
- **[8_rag_web_scrape_basic.py](cci:7://file:///Users/praveenkumar/Desktop/Studies/langchain-tutorial/4_rag/8_rag_web_scrape_basic.py:0:0-0:0)**: Web scraping with basic RAG
- **[8_rag_web_scrape_firecrawl.py](cci:7://file:///Users/praveenkumar/Desktop/Studies/langchain-tutorial/4_rag/8_rag_web_scrape_firecrawl.py:0:0-0:0)**: Advanced web scraping with Firecrawl

## 🛠️ Running the Examples

### Basic RAG
```bash
python 4_rag/1a_rag_basics.py
```

### Conversational RAG
```bash
python 4_rag/7_rag_conversational.py
```

### Web Scraping with RAG
```bash
python 4_rag/8_rag_web_scrape_basic.py
```

### Web Scraping with FireCrawl and RAG
```bash
python 4_rag/8_rag_web_scrape_firecrawl.py
```

## 🔍 Code Explanation

### Key Components

#### Document Loading
```python
from langchain_community.document_loaders import TextLoader
loader = TextLoader("books/langchain_demo.txt")
documents = loader.load()
```

#### Text Splitting
```python
from langchain.text_splitter import CharacterTextSplitter
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
docs = text_splitter.split_documents(documents)
```

#### Embeddings
```python
from langchain_community.embeddings import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
```

#### Vector Store
```python
from langchain_community.vectorstores import Chroma
db = Chroma.from_documents(docs, embeddings, persist_directory="./chroma_db")
```

#### Retrieval QA Chain
```python
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=db.as_retriever()
)
```

### 🌟 Best Practices

- Chunk Size: Adjust based on your document type and model context window
- Metadata: Include relevant metadata for better filtering
- Error Handling: Implement proper error handling for production use
- Caching: Cache embeddings and vector stores for better performance
- Monitoring: Add logging and monitoring for production deployments

### 🚨 Troubleshooting

- API Key Errors
    - Ensure your API keys are correctly set in the 
.env
 file
    - Verify the keys have the correct permissions

### Firecrawl Issues
- Check your Firecrawl API key
- Verify the target website allows web scraping

### Memory Issues
- Reduce chunk size if processing large documents
- Use a smaller embedding model if needed

### 📚 Additional Resources
- LangChain Documentation
- HuggingFace Embeddings
- ChromaDB Documentation
- Firecrawl Documentation

### 🤝 Contributing
- Contributions are welcome! Please feel free to submit a Pull Request.

### 📄 License
- This project is licensed under the MIT License - see the LICENSE file for details.
