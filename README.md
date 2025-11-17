AmbedkarGPT – Intern Task (RAG + LangChain + Ollama)

A simple command-line Q&A system built using:

LangChain

ChromaDB (local vector store)

HuggingFace MiniLM Embeddings

Ollama (Mistral model)

The system loads speech.txt, splits it into chunks, creates embeddings, stores them in Chroma, retrieves relevant context, and generates answers using a local LLM.

Features:
1.Local RAG pipeline
2.No API keys / No internet required
3.Uses Mistral (Ollama)
4.Fast & lightweight
5.Clean and easy to run

Structure:
AmbedkarGPT-Intern-Task/
│
├── main.py
├── speech.txt
├── requirements.txt
├── README.md
└── db/ (auto-created by Chroma)

Rewuirements:
Requirements

1.Python 3.8+
2.Ollama installed
3.At least one local model (mistral / small model for low RAM) 


Setup instructions-


Clone Repository:
git clone <your-repo-url>
cd AmbedkarGPT-Intern-Task

Create virtual environment
python -m venv venv
venv\Scripts\activate   (Windows)

Install dependencies
pip install -r requirements.txt

Install Ollama + Model
ollama pull mistral

Run the Project
python main.py
