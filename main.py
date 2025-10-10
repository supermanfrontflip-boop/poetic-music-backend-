Ifrom fastapi import FastAPI
from pydantic import BaseModel
import os
import openai

app = FastAPI()

# Get OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

class GenerateRequest(BaseModel):
    poem: str
    style: str = "default"

@app.get("/")
def read_root():
    return {"message": "Poetic Music Backend is running!"}

@app.post("/generate")
async def generate_song(req: GenerateRequest):
    """
    Takes a poem and a style, returns generated song lyrics (mocked for now).
    """
    # Create the prompt
    prompt = f"Turn this poem into song lyrics in the style of {req.style}:\n{req.poem}"

    # Generate lyrics using OpenAI
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        lyrics = completion["choices"][0]["message"]["content"]
    except Exception as e:
        lyrics = f"Error generating lyrics: {str(e)}"

    # Mock audio URL (you can replace later)
    audio_url = "https://example.com/audio/mock.mp3"

    return {"lyrics": lyrics, "audio_url": audio_url}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8080)