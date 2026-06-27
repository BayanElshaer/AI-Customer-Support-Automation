from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


SYSTEM_PROMPT = """
You are a ticket classification engine.

Return ONLY ONE WORD.

Valid categories:

Refund
Technical
Shipping
Complaint
Other

Examples:

I want my money back.
Refund

The website crashes when I log in.
Technical

Where is my package?
Shipping

Your support agent was rude.
Complaint

I have a strange question.
Other
"""


def classify_category(message: str) -> str:

    print(f"\nINPUT MESSAGE: {message}")

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        temperature=0,
        max_tokens=10,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": message
            }
        ]
    )

    raw = response.choices[0].message.content

    print(f"RAW CLASSIFIER OUTPUT: [{raw}]")

    category = raw.strip()

    print(f"FINAL CATEGORY: [{category}]")

    allowed = {
        "Refund",
        "Technical",
        "Shipping",
        "Complaint",
        "Other"
    }

    if category not in allowed:
        print("INVALID CATEGORY -> USING OTHER")
        return "Other"

    return category