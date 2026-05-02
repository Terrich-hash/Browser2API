import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "data")
GENERATED_DIR = os.path.join(BASE_DIR, "generated")

HAR_FILE = os.path.join(DATA_DIR, "input.har")
GENERATED_FILE = os.path.join(GENERATED_DIR, "api_routes.py")

IMPORTANT_HEADERS = ["authorization", "cookie", "x-csrf-token"]

IGNORE_TYPES = ["image", "stylesheet", "font"]
IGNORE_DOMAINS = ["google-analytics", "doubleclick"]