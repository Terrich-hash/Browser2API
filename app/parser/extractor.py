from app.core.config import IGNORE_TYPES, IGNORE_DOMAINS, IMPORTANT_HEADERS


def is_valid_request(entry):
    req = entry.get("request", {})
    res = entry.get("response", {})

    mime = res.get("content", {}).get("mimeType", "")

    if any(t in mime for t in IGNORE_TYPES):
        return False

    if any(domain in req.get("url", "") for domain in IGNORE_DOMAINS):
        return False

    return True


def filter_headers(headers):
    return {
        h["name"]: h["value"]
        for h in headers
        if h["name"].lower() in IMPORTANT_HEADERS
    }


def detect_auth_type(headers):
    header_keys = [h["name"].lower() for h in headers]

    if "authorization" in header_keys:
        return "bearer"
    elif "cookie" in header_keys:
        return "cookie"
    return None


def extract_requests(entries):
    extracted = []

    for entry in entries:
        if not is_valid_request(entry):
            continue

        req = entry.get("request", {})

        extracted.append({
            "method": req.get("method"),
            "url": req.get("url", "").split("?")[0],
            "headers": filter_headers(req.get("headers", [])),
            "auth_type": detect_auth_type(req.get("headers", [])),
            "query": {q["name"]: q["value"] for q in req.get("queryString", [])},
            "body": req.get("postData", {}).get("text", {})
        })

    return extracted