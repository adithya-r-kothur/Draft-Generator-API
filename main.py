from fastapi import FastAPI, HTTPException
from models import DraftRequest, DraftResponse
from prompt import PROMPT_TEMPLATE
from llm import call_llm
import json

app = FastAPI(
    title="Adhirame Draft Generator API",
    version="1.0.0"
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/generate-draft", response_model=DraftResponse)
def generate_draft(payload: DraftRequest):
    try:
        prompt = PROMPT_TEMPLATE.format(
            brief=json.dumps(payload.brief, indent=2),
            competitor_blog_text=payload.competitor_blog_text or ""
        )

        markdown = call_llm(prompt)

        return {"markdown": markdown}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
