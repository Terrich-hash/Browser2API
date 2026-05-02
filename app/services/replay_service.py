import httpx


async def replay_request(req, payload=None, headers=None):
    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=req["method"],
            url=req["url"],
            headers=headers or req.get("headers", {}),
            json=payload
        )

    try:
        return response.json()
    except Exception:
        return {"text": response.text}