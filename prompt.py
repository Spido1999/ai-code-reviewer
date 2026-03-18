def build_review_prompt(code, language):
    return f"""You are an expert {language} code reviewer with 10 years of experience.

Review the following {language} code and respond in EXACTLY this JSON format:

{{
    "score": <number from 1-10>,
    "summary": "<one sentence overall assessment>",
    "bugs": [
        "<bug 1 description>",
        "<bug 2 description>"
    ],
    "improvements": [
        "<improvement 1>",
        "<improvement 2>"
    ],
    "fixed_code": "<the corrected version of the code>"
}}

Rules:
- Be specific about line numbers when mentioning bugs
- If no bugs found, return empty list for bugs
- Always provide at least 2 improvements
- fixed_code must be complete working code
- Return ONLY the JSON, no extra text

Code to review:
{code}"""