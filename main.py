from fastapi import FastAPI
from pydantic import BaseModel
from rag_engine import query_llm
from escalation import check_escalation, assign_agent

app = FastAPI()

class Query(BaseModel):
    message: str

@app.post("/chat")
def chat(query: Query):
    if check_escalation(query.message):
        return assign_agent()

    try:
        response = query_llm(query.message)

        return {
            "status": "AI Response",
            "response": str(response)
        }

    except Exception as e: 
        return {
            "status": "Error",
            "response": str(e)
        }     