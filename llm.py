import os
import requests

# OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_API_KEY = "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"
MODEL = os.getenv("MODEL", "openai/gpt-oss-120b:free")

HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://your-render-app.onrender.com",
    "X-Title": "Adhirame Draft Generator"
}


def call_llm(prompt: str) -> str:
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=HEADERS,
        json={
            "model": MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.2
        },
        timeout=90
    )

    data = response.json()

    if "choices" not in data:
        raise RuntimeError(data)

    return data["choices"][0]["message"]["content"]
