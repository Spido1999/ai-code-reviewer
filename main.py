from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
from prompt import build_review_prompt
import json
import re
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
class CodeRequest(BaseModel):
    code: str
    language: str

@app.post("/review")
async def review_code(request: CodeRequest):
    prompt = build_review_prompt(request.code, request.language)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000
    )

    raw = response.choices[0].message.content
    print("RAW RESPONSE:", raw)

    # Extract JSON from response
    raw = raw.strip()
    raw = re.sub(r"```json|```", "", raw).strip()

    result = json.loads(raw)
    return result