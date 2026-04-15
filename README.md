# auto-assist-ai

An AI based customer support assistant that can understand company data (PDFs, images, and websites) and respond to user queries.
It uses a RAG based approach to fetch relevant information and generate accurate responses. The system also identifies critical queries (like complaints or issues) and escalates them to a human support agent.
This project is an attempt to simulate how real world customer support AI systems work.

How To Run :
1. Clone this repository
2. Get a New Terminal from the current location
3. Install all the requriments

Open 3 separate terminals and run the following :
1. Start Ollama (LLM)
   ollama run mistral
2. Start Backend (Fast API)
   uvicorn app:app --reload
3. Start Frontend (Streamlit)
   streamlit run app.py      
