from app.classifier import classify_category
from app.responder import generate_response


def classify_ticket(message: str):

    category = classify_category(message)

    reply = generate_response(
        message,
        category
    )

    return category, reply