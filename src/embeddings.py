from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings

def create_embeddings(df):

    # ✅ Step 1: Convert DataFrame → text
    text_data = df.to_string(index=False)

    print("\n--- TEXT CONVERSION DONE ---")
    print(text_data[:500])   # preview

    # ✅ Step 2: Split into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    texts = text_splitter.split_text(text_data)

    print(f"\n--- CHUNKING DONE ---")
    print(f"Total chunks: {len(texts)}")

    # ✅ Step 3: Load embedding model

    embeddings = HuggingFaceEmbeddings()

    print("\n--- EMBEDDING MODEL LOADED ---")

    return texts, embeddings