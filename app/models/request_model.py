from pydantic import BaseModel
from typing import Dict, Any


class RequestModel(BaseModel):
    method: str
    url: str
    headers: Dict[str, str]
    auth_type: str | None = None
    query: Dict[str, Any] = {}
    body: Dict[str, Any] = {}