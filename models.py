from pydantic import BaseModel
from typing import Dict, Any, Optional


class DraftRequest(BaseModel):
    original_title: str
    brief: Dict[str, Any]
    competitor_blog_text: Optional[str] = ""


class DraftResponse(BaseModel):
    markdown: str
