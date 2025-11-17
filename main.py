from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import Ollama
from langchain.chains import RetrievalQA

def build_rag():
    loader = TextLoader("speech.txt")
    docs = loader.load()

    splitter = CharacterTextSplitter(chunk_size=250, chunk_overlap=40)
    chunks = splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    vectordb = Chroma.from_documents(
        chunks, 
        embedding=embeddings, 
        persist_directory="./db"
    )
    vectordb.persist()

    llm = Ollama(
    model="mistral"
)


    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectordb.as_retriever(),
        return_source_documents=False
    )

    return qa


def main():
    qa = build_rag()
    print("Ask anything about the speech! Type exit to quit.")

    while True:
        q = input("\nQ: ")
        if q.lower() == "exit":
            break

        print("A:", qa(q)["result"])

if __name__ == "__main__":
    main()
