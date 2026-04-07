from data_ingestion import load_pdf, load_website
from rag_engine import create_vector_store

texts = []

# Add PDF
texts.extend([doc.page_content for doc in load_pdf("data/docs/sample.pdf")])

# Add website
texts.append(load_website("https://example.com"))

create_vector_store(texts)

print("Vector DB Created")