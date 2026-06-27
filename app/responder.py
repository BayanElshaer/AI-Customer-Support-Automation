from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_response(
    message: str,
    category: str
):

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        temperature=0.3,
        messages=[
            {
                "role": "system",
                "content": f"""
You are a professional customer support agent.

The ticket category is:

{category}

Write a short, helpful, professional reply.

Do not mention internal classifications.
"""
            },
            {
                "role": "user",
                "content": message
            }
        ]
    )

    return (
        response
        .choices[0]
        .message
        .content
        .strip()
    )