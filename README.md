# AmbedkarGPT – Intern Task

A **RAG-based Q&A system** built using:
- LangChain  
- ChromaDB for vector store  
- Sentence-Transformers (MiniLM) for embeddings  
- Ollama (Mistral model) as the local LLM  

---

##  Project Overview

This project enables you to ask questions about Dr. B. R. Ambedkar’s speech (in `speech.txt`) via a command-line interface.  
It does:
1. Load text  
2. Split into chunks  
3. Embed with MiniLM  
4. Store vectors in ChromaDB  
5. Use a retriever to find relevant chunks  
6. Use Mistral (Ollama) to answer based on retrieved context  

---

## Repository Structure

AmbedkarGPT-Intern-Task/
│
├── main.py # RAG logic
├── speech.txt # Text data
├── requirements.txt # Python deps
├── README.md # This file
└── db/ # Vector store directory (auto-created)



---

## 🛠 Requirements & Setup

1. **Install Ollama**  
   Make sure Ollama is installed and running.

2. **Pull Mistral Model**  
   ```bash
   ollama pull mistral

3. **Create Virtual Environment & Install Dependencies**
python -m venv venv  
source venv/bin/activate  # Linux/macOS  
venv\Scripts\activate     # Windows  
pip install -r requirements.txt

How to RUN?


python main.py




