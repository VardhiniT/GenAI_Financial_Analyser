from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEmbeddings
from datetime import date
from company_mapper import get_ticker_from_query

from data_storage import update_stock_data
from analytics import compute_metrics, format_metrics, compare_companies

from dotenv import load_dotenv

load_dotenv()
import os
print("KEY:", os.getenv("OPENAI_API_KEY"))

def run_rag():

    print("🔥 RAG STARTED")

    # ✅ Load embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-mpnet-base-v2"
    )

    # ✅ Load vector DB
    vector_db = Chroma(
        persist_directory="vector_db",
        embedding_function=embeddings
    )

    print("\n--- VECTOR DB LOADED ---")

    # ✅ Retriever
    retriever = vector_db.as_retriever(search_kwargs={"k": 3})

    # ✅ LLM
    llm = ChatOpenAI(
        temperature=0,
        model="gpt-4o-mini"
    )

    data_cache = {}
    metrics_cache = {}
    last_updated = {}

    # ✅ Manual RAG loop (NEW METHOD)
    while True:
        query = input("\nAsk a question (type 'exit' to stop): ")

        if query.lower() == "exit":
            print("👋 Exiting RAG...")
            break

        tickers = get_ticker_from_query(query)

        if len(tickers) == 1:

            ticker = tickers[0]

            # 🔥 Refresh logic (daily)
            if ticker not in data_cache or last_updated.get(ticker) != date.today():

                print("📥 Fetching fresh data...")

                df = update_stock_data(ticker)

                data_cache[ticker] = df
                metrics_cache[ticker] = compute_metrics(df)
                last_updated[ticker] = date.today()

            else:
                print("⚡ Using cached data...")

            metrics = metrics_cache[ticker]
            analysis_text = format_metrics(ticker, metrics)
        else:
            analysis_text = "No specific company identified. Answer using context."

        # 🔹 Step 1: Retrieve relevant docs
        docs = retriever.invoke(query)

        # 🔹 Step 2: Combine context
        context = "\n\n".join([doc.page_content for doc in docs])

        prompt = f"""
        You are a financial analyst.

        Use BOTH retrieved data and analytical insights.

        Retrieved Context:
        {context}

        Analytical Insights:
        {analysis_text}

        Question:
        {query}

        Give a clear, data-driven answer.
        """

        # 🔹 Step 4: Get answer
        response = llm.invoke(prompt)

        print("\n🤖 Answer:\n", response.content)


if __name__ == "__main__":
    run_rag()