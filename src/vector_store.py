from langchain_community.vectorstores import Chroma

def create_vector_store(texts, embeddings):

    # Create vector DB
    vector_db = Chroma.from_texts(
        texts=texts,
        embedding=embeddings,
        persist_directory="vector_db"
    )

    vector_db.persist()   # ✅ ADD THIS LINE
    
    print("\n--- VECTOR DB CREATED ---")

    return vector_db