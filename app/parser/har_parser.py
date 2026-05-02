import json


def load_har(file_path: str):
    encodings = ["utf-8", "utf-16", "latin-1"]

    for enc in encodings:
        try:
            with open(file_path, "r", encoding=enc) as f:
                return json.load(f)
        except Exception:
            continue

    raise ValueError("Failed to read HAR file. Invalid encoding or corrupted file.")


def get_entries(har_data):
    return har_data.get("log", {}).get("entries", [])