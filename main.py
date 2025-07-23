import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_community.llms import Ollama

app = FastAPI(
    title="Legal RAG API",
    description="An API for querying a local LLM for legal research.",
    version="1.0.0",
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

try:
    llm = Ollama(model="tinyllama")
    print("Ollama model 'tinyllama' loaded successfully.")
except Exception as e:
    print(f"Error loading Ollama model: {e}")
    llm = None

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
async def process_query(request: QueryRequest):
    """
    Receives a query from the frontend, sends it to Ollama,
    and returns the model's response.
    """
    if llm is None:
        return {"response": "Error: Ollama model is not available."}
        
    try:
        user_query = request.query
        print(f"Received query: {user_query}")

        response_text = llm.invoke(user_query)
        print(f"Ollama response: {response_text}")

        return {"response": response_text}
        
    except Exception as e:
        print(f"An error occurred during query processing: {e}")
        return {"response": f"An error occurred on the server: {e}"}

if __name__ == "__main__":
    print("Starting FastAPI server...")
    uvicorn.run(app, host="127.0.0.1", port=8000)
