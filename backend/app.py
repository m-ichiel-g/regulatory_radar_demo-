from fastapi import FastAPI
from supabase import create_client, Client
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

# Read env variables
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

# Init Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# FastAPI app
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Backend is running 🚀"}

@app.get("/themes")
def get_themes():
    data = supabase.table("themes").select("*").execute()
    return data.data

@app.post("/publications")
def add_publication(title: str, url: str):
    data = supabase.table("publications").insert({
        "title": title,
        "url": url
    }).execute()
    return data.data
