from fastapi import FastAPI
from supabase import create_client, Client
import os

app = FastAPI()
supabase: Client = None

@app.on_event("startup")
def startup_event():
    global supabase
    SUPABASE_URL = os.environ.get("SUPABASE_URL")
    SUPABASE_KEY = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")

    print("SUPABASE_URL:", SUPABASE_URL)
    print("SUPABASE_KEY present?", bool(SUPABASE_KEY))

    if not SUPABASE_URL or not SUPABASE_KEY:
        raise RuntimeError("Missing SUPABASE environment variables")

    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

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
    print(data)
    return data.data
