from pathlib import Path
from typing import List, Any
from langchain_community.document_loaders import PyMuPDFLoader

def load_document(data_dir:str) -> List[Any]:
    data_path = Path(data_dir).resolve()
    print(f"[DEBUG] Data Path: {data_dir}")
    documents = []

    pdf_files = list(data_path.glob("**/*.pdf"))
    print(f"[DEBUG] PDF files {len(pdf_files)} Found, PDF files {[str(s) for s in pdf_files]}")
    for pdf_file in pdf_files:
        print(f"[DEBUG] loading file {pdf_file}")
        try:
            loader = PyMuPDFLoader(str(pdf_file))
            loaded = loader.load()
            print(f"[DEBUG] Loaded {loaded} from docs {pdf_file}")
            documents.extend(loaded)
        except Exception as e:
            print(f"[ERROR] Failed to load PDF {pdf_file}: {e}") 

    print(f"[DEBUG] Total loaded documents: {len(documents)}")
    return documents


if __name__ == "__main__":
    docs = load_document("data")
    print(f"Loaded {len(docs    )} documents.")
    print(f"Example docs {docs[0] if docs else None}")  