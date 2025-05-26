# Crawl4AI RAG Backend

This is the backend for the Crawl4AI Retrieval Augmented Generation (RAG) system. It allows you to crawl web pages, chunk and embed their content, store them in a Supabase/Postgres database with pgvector, and retrieve relevant information using OpenAI's language models.

## Features
- Crawl web pages and extract content
- Chunk and embed text using OpenAI embeddings
- Store documents and embeddings in Supabase/Postgres
- Retrieve relevant chunks using vector similarity search
- Generate answers using OpenAI GPT models

## Prerequisites
- Python 3.8+
- A Supabase project with pgvector enabled
- OpenAI API key

## Setup

1. **Clone the repository:**
   ```sh
   git clone <your-repo-url>
   cd Crawl4AI-RAG/backend
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   Create a `.env` file in the `backend` directory with the following:
   ```env
   SUPABASE_DB_URL=postgresql://<user>:<password>@<host>:<port>/<dbname>
   OPENAI_API_KEY=sk-...
   ```
   Replace with your actual Supabase connection string and OpenAI API key.

4. **Run the FastAPI server:**
   ```sh
   uvicorn main:app --reload
   ```
   The API will be available at `http://localhost:8000`.

## Endpoints

### `/crawl` (POST)
Crawl a web page, chunk and embed its content, and store in the database.
- **Request body:** JSON with a `url` field (string)
- **Example:**
  ```json
  {
    "url": "https://example.com"
  }
  ```
- **Response:**
  ```json
  {
    "status": "Crawl completed for",
    "url": "https://example.com"
  }
  ```

### `/retrieve` (POST)
Retrieve relevant chunks and generate an answer using OpenAI.
- **Request body:** JSON with a `query` field (string)
- **Example:**
  ```json
  {
    "query": "What is the main topic of the document?"
  }
  ```
- **Response:**
  ```json
  {
    "answer": "...",
    "sources": [
      {
        "document_id": "...",
        "chunk_index": 0,
        "content": "...",
        "similarity": 0.123
      },
      ...
    ]
  }
  ```

## Notes
- Make sure your Supabase database has the correct schema and the `pgvector` extension enabled.
- The backend uses OpenAI for both embeddings and answer generation.
- For development, you can use the interactive docs at `http://localhost:8000/docs`.

## License
MIT 