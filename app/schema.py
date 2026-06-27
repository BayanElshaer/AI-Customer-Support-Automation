from pydantic import BaseModel
from enum import Enum
from typing import Optional

class TicketRequest(BaseModel):
    from_email: Optional[str] = None
    subject: Optional[str] = None
    message: str

class Category(str, Enum):
    Refund = "Refund"
    Technical = "Technical"
    Shipping = "Shipping"
    Complaint = "Complaint"
    Other = "Other"

class Status(str, Enum):
    OPEN = "OPEN"
    AUTO_RESOLVED = "AUTO_RESOLVED"
    WAITING_FOR_CUSTOMER = "WAITING_FOR_CUSTOMER"
    ESCALATED = "ESCALATED"
    CLOSED = "CLOSED"

class TicketResponse(BaseModel):
    category: Category
    response: str
    status: Status

class TicketUpdate(BaseModel):
    status: Status