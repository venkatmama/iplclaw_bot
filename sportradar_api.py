import os
import httpx

API_KEY = os.getenv("SPORTRADAR_API_KEY")
BASE_URL = "https://api.sportradar.com/cricket/trial/v4/en"

# 🔴 IMPORTANT: set manually for now
MATCH_ID = "sr:match:12345678"

async def get_match():
    return MATCH_ID

async def fetch_timeline(match_id):
    url = f"{BASE_URL}/matches/{match_id}/timeline.json?api_key={API_KEY}"

    async with httpx.AsyncClient() as client:
        res = await client.get(url)

        if res.status_code != 200:
            print("API ERROR:", res.status_code, res.text)
            return {}

        return res.json()
