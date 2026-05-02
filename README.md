# Browser2API 

Convert browser network recordings (HAR files) into reusable API endpoints automatically.

---

##  Overview

Browser2API is a developer tool that takes a HAR (HTTP Archive) file exported from browser DevTools and transforms captured network requests into dynamic FastAPI endpoints.

It enables:

* Reverse engineering APIs from frontend applications
* Rapid backend prototyping
* API testing and replay

---

##  Features

*  Upload HAR files directly
*  Extract meaningful API requests (filters out noise like images, analytics)
*  Smart endpoint naming (no more `/endpoint_0`)
*  Dynamic authentication handling (Bearer tokens, cookies)
*  Auto-generate FastAPI routes
*  Replay captured requests using httpx
*  Preview generated API code

---

##  Project Structure

```
browser2api/
│
├── app/
│   ├── main.py              # FastAPI entry point
│   ├── core/               # Config & constants
│   ├── parser/             # HAR parsing & extraction
│   ├── generator/          # API code generation
│   ├── services/           # Request replay logic
│   ├── models/             # Data models
│   └── utils/              # Helpers (cleaning, naming)
│
├── data/                   # HAR input storage
├── generated/              # Auto-generated APIs
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

##  Installation

```bash
git clone https://github.com/Terrich-hash/browser2api.git
cd browser2api
pip install -r requirements.txt
```

---

## 🚀 Run the Server

```bash
uvicorn app.main:app --reload
```

Open:
👉 http://127.0.0.1:8000/docs

---

## 🔄 Usage Workflow

### 1. Export HAR from browser

Using Chrome DevTools:

1. Open **Network tab**
2. Perform desired action (e.g., search flights)
3. Right-click → **Save all as HAR with content**

---

### 2. Upload HAR file

```http
POST /upload-har/
```

---

### 3. Generate APIs

```http
POST /generate/
```

---

### 4. Preview generated code

```http
GET /preview/
```

Generated APIs will be saved in:

```
generated/api_routes.py
```

---

##  Authentication Handling

Browser2API detects and supports:

* Bearer Token (`Authorization`)
* Cookie-based sessions

Generated endpoints accept auth dynamically via headers:

```http
Authorization: Bearer <token>
Cookie: session_id=...
```

---

##  Smart Endpoint Naming

Instead of generic routes:

```
/endpoint_0
```

Browser2API generates:

```
/post_flights_search
/get_user_profile
/post_booking_create
```

---

##  Limitations

* HAR files must be valid JSON (not corrupted or binary)
* Auth tokens may expire (manual refresh required)
* Some APIs use anti-bot protection or dynamic signatures
* Not all requests are replayable outside browser context

---

##  Future Improvements

* Dynamic parameter detection (auto-convert static values to inputs)
* Token/session auto-refresh
* OpenAPI / Postman export
* Chrome Extension for live capture
* UI dashboard for visualization and testing

---

##  Tech Stack

* FastAPI
* httpx
* Pydantic
* Python

---

##  Use Cases

* Reverse engineer frontend APIs
* Build mock backends
* Debug network flows
* Rapid prototyping

---

##  Author

Terrich

---

## ⭐ Contributing

Pull requests are welcome. For major changes, open an issue first to discuss what you’d like to change.

---

## 📜 License

MIT License
