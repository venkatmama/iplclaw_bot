import httpx

# Replace with live match ID (you can dynamically fetch later)
MATCH_ID = "ipl_match_id_here"

async def fetch_commentary():
    url = f"https://www.cricbuzz.com/api/cricket-match/commentary/{MATCH_ID}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    async with httpx.AsyncClient() as client:
        res = await client.get(url, headers=headers)
        return res.json()
