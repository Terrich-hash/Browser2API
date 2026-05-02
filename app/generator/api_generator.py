from app.utils.cleaner import generate_endpoint_name


def build_auth_params(auth_type):
    if auth_type == "bearer":
        return "authorization: str = Header(None)"
    elif auth_type == "cookie":
        return "cookie: str = Header(None)"
    return ""


def build_auth_headers(auth_type):
    if auth_type == "bearer":
        return '{"Authorization": authorization}'
    elif auth_type == "cookie":
        return '{"Cookie": cookie}'
    return "{}"


def generate_fastapi_routes(requests):
    code = """
from fastapi import APIRouter, Request, Header
import httpx

router = APIRouter()
"""

    used_names = set()

    for i, req in enumerate(requests):
        method = req["method"].lower()

        name = generate_endpoint_name(req["method"], req["url"])

        if name in used_names:
            name = f"{name}_{i}"
        used_names.add(name)

        auth_param = build_auth_params(req.get("auth_type"))
        auth_headers = build_auth_headers(req.get("auth_type"))

        code += f"""
@router.{method}("/{name}")
async def {name}(request: Request{', ' + auth_param if auth_param else ''}):
    payload = None

    if request.method != "GET":
        try:
            payload = await request.json()
        except:
            payload = None

    headers = {auth_headers}

    async with httpx.AsyncClient() as client:
        response = await client.request(
            method="{req['method']}",
            url="{req['url']}",
            headers=headers,
            json=payload
        )

    try:
        return response.json()
    except:
        return {{"text": response.text}}
"""

    return code