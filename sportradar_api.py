import os
import httpx

API_KEY = os.getenv("SPORTRADAR_API_KEY")

# Replace with your match ID
MATCH_ID = "YOUR_MATCH_ID"

async def fetch_ball_data():
    url = f"https://api.sportradar.com/cricket/trial/v4/en/matches/{MATCH_ID}/timeline.json?api_key={API_KEY}"

    async with httpx.AsyncClient() as client:
        res = await client.get(url)
        return res.json()
