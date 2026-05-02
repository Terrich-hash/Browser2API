import json
import re
from urllib.parse import urlparse


def normalize_body(body):
    if not body:
        return {}

    try:
        return json.loads(body)
    except Exception:
        return {"raw": body}


def generate_endpoint_name(method: str, url: str):
    parsed = urlparse(url)
    path = parsed.path

    # remove numeric ids
    path = re.sub(r'/\d+', '', path)

    parts = [p for p in path.split("/") if p]

    if not parts:
        return f"{method.lower()}_root"

    name_parts = parts[-2:]
    name = "_".join(name_parts)

    return f"{method.lower()}_{name}"


def clean_requests(requests):
    cleaned = []

    for req in requests:
        cleaned.append({
            "method": req["method"],
            "url": req["url"],
            "headers": req["headers"],
            "auth_type": req.get("auth_type"),
            "query": req["query"],
            "body": normalize_body(req["body"])
        })

    return cleaned