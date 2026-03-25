GenAI Financial Analyzer

-> Overview -
Traditional financial analysis is often static and requires manual interpretation of data. This project builds an end-to-end GenAI pipeline that automates this process by combining financial analytics with intelligent retrieval and language model reasoning. The system computes key financial metrics such as returns, volatility, and growth, transforms structured data into embeddings, retrieves relevant company information using vector similarity, and generates context-aware financial insights using a large language model. This enables intelligent company comparison and automated financial reasoning without the need for model fine-tuning.

-> Key Features - 
•	Financial metric computation including returns, volatility, and growth trends
•	Embedding-based semantic search for company data
•	RAG pipeline for contextual financial insight generation
•	Company comparison using LLM-based reasoning
•	Modular architecture for scalability and maintainability

-> Financial Metrics Used -
The system uses several key financial metrics to generate insights:
•	Daily Returns: Measures percentage change in stock prices
•	1-Year Growth: Evaluates performance over approximately 252 trading days
•	5-Year Growth: Captures long-term performance trends
•	Volatility: Represents risk using the standard deviation of returns
•	Average Return: Indicates mean performance over time

-> Project Structure - 
The project is organized into modular components:
•	analytics.py: Computes financial metrics such as returns, volatility, and growth
•	embeddings.py: Converts structured data into vector embeddings
•	vector_store.py: Handles vector database storage and retrieval
•	rag_pipeline.py: Implements the core RAG pipeline
•	data_loader.py: Loads financial datasets
•	data_storage.py: Manages processed data
•	company_mapper.py: Maps user queries to specific companies

-> Environment Variables -
The project requires an API key for the language model. Create a .env file in the root directory and add your API key. A template file (.env.example) is provided for reference. Ensure that the .env file is not committed to version control.

-> Example Use Cases -
•	Comparing companies based on growth and risk profiles
•	Generating automated financial summaries
•	Identifying high-growth versus high-volatility stocks
•	Supporting investment decision-making with AI-generated insights

-> Future Improvements - 
•	Integration with real-time financial APIs
•	Addition of advanced financial metrics such as Sharpe Ratio and Beta
•	Deployment as a web application using frameworks like Streamlit or FastAPI
•	Improved evaluation mechanisms for generated outputs
