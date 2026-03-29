import os
import httpx

API_KEY = os.getenv("SPORTRADAR_API_KEY")
BASE_URL = "https://api.sportradar.com/cricket/trial/v4/en"

async def get_live_match():
    url = f"{BASE_URL}/schedules/live/matches.json?api_key={API_KEY}"

    async with httpx.AsyncClient() as client:
        res = await client.get(url)
        data = res.json()

    for match in data.get("matches", []):
        if "IPL" in match.get("tournament", {}).get("name", ""):
            return match.get("id")

    return None

async def fetch_timeline(match_id):
    url = f"{BASE_URL}/matches/{match_id}/timeline.json?api_key={API_KEY}"

    async with httpx.AsyncClient() as client:
        res = await client.get(url)
        return res.json()
