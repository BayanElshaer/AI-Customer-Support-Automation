from fastapi import FastAPI, HTTPException, status
from contextlib import asynccontextmanager
from rich   import print, panel
from sqlmodel import select
from app.schema import TicketRequest, TicketResponse, TicketUpdate, Status
from app.ai_service import classify_ticket

from app.database import  create_db_table, sessionDepends
from app.models import Ticket

# Base.metadata.create_all(bind=engine)

@asynccontextmanager
async def lifesapn_handler(app: FastAPI):
    print(panel.Panel("Server started...", border_style="green"))
    create_db_table()
    yield
    print(panel.Panel("...Server stopped", border_style="red"))

app = FastAPI(
    lifespan=lifesapn_handler,
    title="Customer Support Ticket Classifier",
    version="1.0.0",
)

@app.post("/process", response_model=TicketResponse)
def classify(request: TicketRequest, session: sessionDepends):
    category, reply = classify_ticket(request.message)

    ticket = Ticket(
        customer_name=None,
        email=request.from_email,
        subject=request.subject,
        message=request.message,
        category=category,
        response=reply,
        status=Status.OPEN,
    )

    session.add(ticket)
    session.commit()
    session.refresh(ticket)

    return TicketResponse(
        category=category,
        response=reply,
        status = ticket.status
    )

@app.patch("/tickets/{id}", response_model=TicketResponse)
def update_ticket_status(id: int, update: TicketUpdate, session: sessionDepends):
    # Clean up the string values if they contain leading colons or spaces
    ticket = session.get(Ticket, id)
    # if ticket.category and isinstance(ticket.category, str):
    #     ticket.category = ticket.category.lstrip(": ").strip()
        
    # if ticket.status and isinstance(ticket.status, str):
    #     ticket.status = ticket.status.lstrip(": ").strip()
    
    if ticket is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Ticket #{id} not found"
        )
    
    update = update.model_dump(exclude_none=True)
    if not update:
        raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail="No data provided to update"
        )
    ticket.sqlmodel_update(update)
    session.add(ticket)
    session.commit()
    session.refresh(ticket)
    return ticket

@app.get("/tickets/{ticket_id}", response_model=TicketResponse)
def get_tickets(ticket_id: int, session: sessionDepends):
    ticket = session.get(Ticket, ticket_id)
    if ticket is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Ticket #{ticket_id} not found"
        )

    return ticket


@app.delete("/tickets/{ticket_id}")
def delete_ticket(ticket_id: int, session: sessionDepends):
    ticket = session.get(Ticket, ticket_id)
    if ticket is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Ticket #{ticket_id} not found"
        )
    session.delete(ticket)
    session.commit()

    return {"detail": f"Ticket with id#{ticket_id} was deleted"}

@app.get("/tickets")
def get_all_tickets(session: sessionDepends):
    tickets = session.exec(select(Ticket)).all()
    return tickets