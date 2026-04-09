<<<<<<< HEAD
# 📊 Financial Intelligence System using RAG + Analytics

## 1. Introduction

This project implements a Retrieval-Augmented Generation (RAG) based financial analysis system that combines financial data retrieval, vector-based semantic search, and LLM-based reasoning.

Unlike traditional RAG systems, this project integrates an analytics layer and stores both raw financial data and computed metrics into a unified document store, making the system fully query-driven.

---

## 2. Objective

* Build a fully queryable RAG-based financial system
* Enable dynamic retrieval of both raw and computed financial insights
* Integrate LLM-based query understanding (entity + intent extraction)
* Ensure efficiency using caching and controlled data refresh

---

## 3. 🧩 Project Architecture

```mermaid
flowchart TD

A[User Query] --> B[LLM Query Understanding]
B --> C[Extract Company + Intent]

C --> D{Cache Check (24 hrs)}

D -->|Cache Valid| E[Load Data from Cache]
D -->|Cache Expired / Not Present| F[Fetch Data from API]

F --> G[Store/Update CSV (5 yrs)]
G --> H[Compute Analytics (Pandas)]

E --> H

H --> I[Convert to Text (Raw + Analytics)]
I --> J[Chunking]
J --> K[Embeddings (HuggingFace)]
K --> L[Vector DB (ChromaDB)]

A --> M[Retriever]
L --> M

M --> N[Top-K Relevant Chunks]

N --> O[Prompt Construction]
O --> P[LLM (GPT-4o mini)]
P --> Q[Final Answer]
```

---

## 4. Key Design Flow

### Step 1: Query Understanding

* User query is passed to LLM
* LLM extracts:

  * Company name
  * Query intent (analysis / descriptive / comparison)

---

### Step 2: Cache Mechanism (24-hour Refresh)

* System checks:

  * If data exists in cache
  * If last update is within 24 hours

#### If cache is valid:

* Use existing data
* Avoid API calls

#### If cache expired:

* Fetch fresh data
* Update CSV
* Recompute analytics

---

### Step 3: Data Preparation

* Raw financial data fetched (5 years history)
* Analytics computed:

  * Growth
  * Volatility
  * Returns

---

### Step 4: Unified Document Creation

Both are combined:

* Raw financial data
* Computed analytics

Converted into:

👉 Text documents → chunked → embedded

---

### Step 5: Vector Storage

* Stored in ChromaDB
* Enables semantic retrieval

---

### Step 6: Retrieval (RAG)

* Query → embedding
* Top-K relevant chunks retrieved
* Only relevant portions passed to LLM

---

### Step 7: Response Generation

* LLM generates answer using:

  * Retrieved context
* No direct injection of analytics
* Fully retrieval-driven system

---

## 5. Project Structure

* `rag_pipeline.py` – Main pipeline (query → retrieval → response)
* `data_storage.py` – Handles CSV storage and updates
* `analytics.py` – Computes financial metrics
* `embeddings.py` – Text chunking and embedding generation
* `vector_store.py` – Vector DB creation (ChromaDB)
* `data/` – Cached financial data (CSV)
* `vector_db/` – Persisted embeddings

---

## 6. Core Components

### Data Layer

* API-based financial data (via yfinance)
* Stored locally as CSV
* Updated only when cache expires

---

### Analytics Layer

* Uses Pandas for deterministic computation
* Converts structured metrics into text format
* Stored alongside raw data

---

### Retrieval Layer (RAG)

* Uses semantic similarity search
* Retrieves only relevant chunks

---

### LLM Layer

* Model: GPT-4o mini
* Temperature = 0
* Used for:

  * Query understanding
  * Final response generation

---

## 7. Design Decisions

### Why Full RAG (Including Analytics)?

* Makes entire system queryable
* Avoids unnecessary prompt injection
* Enables flexible querying of both raw and computed data

---

### Why Caching?

* Reduces API calls
* Improves latency
* Ensures data consistency within a defined time window

---

### Why LLM for Query Understanding?

* Handles flexible user queries
* Avoids rigid rule-based mapping
* Supports multi-intent queries

---

## 8. Advantages

* Fully query-driven system
* Unified knowledge base (raw + analytics)
* Reduced prompt noise
* Efficient via caching
* Scalable architecture

---

## 9. Limitations

* Re-embedding required when data updates
* Retrieval quality depends on chunking
* No real-time streaming data
* LLM dependency for query parsing

---

## 10. Future Improvements

* Incremental embedding updates
* Multi-company query support
* Visualization dashboard
* Advanced query decomposition
* Hybrid structured + vector retrieval

---

## 11. Conclusion

This project demonstrates a fully queryable RAG-based financial system where both raw financial data and computed analytics are embedded and retrieved dynamically.

It highlights how combining retrieval, computation, and LLM reasoning leads to a scalable and efficient AI system for financial insights.

---
