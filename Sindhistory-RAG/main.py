import os
from google import genai
from google.genai import types
from src.vector_store import FaissVectorStore  
from src.data_loader import load_document      
from dotenv import load_dotenv
load_dotenv()
# --- CONFIGURATION ---
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY") 
DATA_PATH = os.environ.get("DATA_PATH")              
DB_DIR = os.environ.get("DB_DIR")

def get_rag_response(user_query, vector_store, client):
    """Retrieves context from FAISS and generates an answer via Gemini."""
    
    # 1. Retrieve (using your existing query method)
    print(f"[INFO] Searching local database...")
    search_results = vector_store.query(user_query, top_k=5)
    
    # 2. Extract text from metadata
    context_list = [res['metadata']['text'] for res in search_results if res['metadata']]
    context_text = "\n\n---\n\n".join(context_list)
    
    if not context_text:
        return "I couldn't find any relevant information in the local database."

    # 3. Construct Prompt
    prompt = f"""
    You are a professional assistant. Answer the question using ONLY the context provided below.
    If the context does not contain the answer, state that you don't know.
    
    CONTEXT:
    {context_text}
    
    USER QUESTION: 
    {user_query}
    """
    
    # 4. Generate using Gemini 2.0 Flash
    print(f"[INFO] Sending to Gemini...")
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.1, # Low temperature for factual accuracy
            max_output_tokens=500
        )
    )
    
    return response.text

def main():
    client = genai.Client(api_key=GOOGLE_API_KEY)
    
    store = FaissVectorStore(persist_dir=DB_DIR)

    if not os.path.exists(os.path.join(DB_DIR, "faiss.index")):
        print("[INFO] Database not found. Building from documents...")
        docs = load_document(DATA_PATH)
        store.build_from_documents(docs)
    else:
        print("[INFO] Loading existing database...")
        store.load()

    
    print("\n" + "="*30)
    print("RAG System Ready! Type 'exit' to stop.")
    print("="*30)

    while True:
        query = input("\nYour Question: ")
        if query.lower() in ['exit', 'quit']:
            break
        
        answer = get_rag_response(query, store, client)
        print(f"\n[AI]: {answer}")

if __name__ == "__main__":
    main()