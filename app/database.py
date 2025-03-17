import chromadb

try:

    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    print("Chroma db connected successfully ")
    
except Exception as e:
    print("chroma db connection failed {e}")

