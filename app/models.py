from typing import Optional
from sqlmodel import SQLModel, Field
from .schema import Status


class Ticket(SQLModel, table=True):
    __tablename__ = "tickets"

    id: int | None = Field(default=None, primary_key=True)

    customer_name: Optional[str] = Field(default=None)
    email: Optional[str] = Field(default=None)
    subject: Optional[str] = Field(default=None)
    message: str

    category: str
    response: str

    status: Status = Field(default=Status.OPEN)
    created_at: Optional[str] = Field(default=None)