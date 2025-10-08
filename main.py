from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os
from transformers import pipeline

app = FastAPI()

# OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Lightweight music generation model
musicgen = pipeline("text-to-audio", "facebook/musicgen-small")

class GenerateRequest(BaseModel):
    poem: str
    style: str = "default"

@app.post("/generate")
async def generate_song(req: GenerateRequest):
    # Generate lyrics
    prompt = f"Turn this poem into song lyrics in style {req.style}:\n{req.poem}"
    lyrics = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )["choices"][0]["message"]["content"]

    # Generate music (mock audio URL for now)
    audio = musicgen(req.poem, forward_params={"do_sample": True})
    audio_url = "https://example.com/audio/mock.mp3"

    return {"lyrics": lyrics, "audio_url": audio_url}
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
