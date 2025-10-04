# 🎵 Poetic Music Generator Backend

FastAPI backend for generating lyrics (OpenAI) and music (MusicGen).

## 🚀 Deploy to Railway
Click the button below to deploy:

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/new?repo=https://github.com/YOUR_USERNAME/poetic-music-backend)

## Setup
1. Add environment variable `OPENAI_API_KEY` in Railway dashboard
2. Railway will build and give you a public URL like:
   https://poetic-music-backend.up.railway.app/generate

## Example Request
```bash
curl -X POST https://YOUR_URL/generate -H "Content-Type: application/json" -d '{"poem": "Roses are red...", "style": "rock"}'
```
