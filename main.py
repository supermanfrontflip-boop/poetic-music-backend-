from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

# Create FastAPI app
app = FastAPI(
    title="Extraordinary Healing API",
    description="A simple FastAPI service deployed on Railway",
    version="1.0.0",
)

# Allow all origins (for testing or frontend access)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Extraordinary Healing API!"}

# Example hello endpoint
@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}! You’re visiting from Railway!"}

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}

# Main entrypoint (for local & Railway)
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)