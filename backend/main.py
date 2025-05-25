from fastapi import FastAPI
import os
import psycopg2
import asyncio
from crawl4ai import AsyncWebCrawler

app = FastAPI()

# Supabase connection details (get these from your Supabase project settings)
SUPABASE_DB_URL = os.getenv("SUPABASE_DB_URL")  # e.g., "postgresql://user:password@host:port/dbname"

def save_to_supabase(url, content):
    conn = psycopg2.connect(SUPABASE_DB_URL)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO documents (source_url, content) VALUES (%s, %s)",
        (url, content)
    )
    conn.commit()
    cur.close()
    conn.close()

async def crawl_and_store(url):
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=url)
        # result.markdown contains the extracted content
        save_to_supabase(url, result.markdown)

@app.get("/")
def read_root():
    return {"message": "Welcome to Crawl4AI RAG Backend!"}

@app.post("/crawl")
async def start_crawl(url: str):
    await crawl_and_store(url)
    return {"status": "Crawl completed for", "url": url} 