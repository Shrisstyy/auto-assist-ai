from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama
from langchain_text_splitters import CharacterTextSplitter

embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def create_vector_store(texts):
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.create_documents(texts)

    vectorstore = FAISS.from_documents(docs, embedding)
    vectorstore.save_local("data/vectorstore")

def load_vector_store():
    return FAISS.load_local(
        "data/vectorstore",
        embedding,
        allow_dangerous_deserialization=True
    )
def query_llm(query):
    db = load_vector_store()
    docs = db.similarity_search(query)

    context = "\n".join([doc.page_content for doc in docs])

    llm = Ollama(model="mistral")

    prompt = f"""
    You are a professional company assistant.
    Answer like a human support agent.

    Context:
    {context}

    Question:
    {query}
    """

    return str(llm.invoke(prompt))