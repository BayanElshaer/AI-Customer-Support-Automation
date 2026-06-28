# AI-Customer-Support-Automation

An AI-powered customer support platform that automates ticket classification, response generation, and workflow orchestration using Large Language Models (LLMs), FastAPI, n8n, SQLModel, and Docker.

The project demonstrates how modern AI services can be integrated into backend systems to reduce manual support effort, improve response consistency, and automate business workflows.

---

## Features

### AI Ticket Classification

Automatically classifies incoming support requests into predefined categories:

* Refund
* Technical
* Shipping
* Complaint
* Other

### AI-Generated Responses

Generates professional customer support replies using Llama 3.1 through the Groq API.

### REST API Backend

Built with FastAPI and fully documented through Swagger UI.

### Workflow Automation

Uses n8n webhooks and HTTP workflows to automate ticket processing pipelines.

### Database Persistence

Stores tickets and their lifecycle information using SQLModel and SQLite.

### Dockerized Architecture

Runs both the API service and n8n inside Docker containers using Docker Compose.

---

# System Architecture

```text
Client
   │
   ▼
n8n Webhook
   │
   ▼
HTTP Request Node
   │
   ▼
FastAPI Backend
   │
   ├── AI Classification (Groq + Llama 3.1)
   ├── Response Generation
   └── SQLModel + SQLite
   │
   ▼
JSON Response
   │
   ▼
n8n Respond to Webhook
```

---

# Tech Stack

| Category               | Technologies                    |
| ---------------------- | ------------------------------- |
| Language               | Python 3.13                     |
| Backend Framework      | FastAPI                         |
| Data Validation        | Pydantic                        |
| Database ORM           | SQLModel                        |
| Database               | SQLite                          |
| AI/LLM                 | Groq API (Llama 3.1 8B Instant) |
| Workflow Automation    | n8n                             |
| Containerization       | Docker                          |
| Orchestration          | Docker Compose                  |
| Environment Management | python-dotenv                   |

---

# Project Structure

```text
AI_customer_support_automation/
│
├── app/
│   ├── main.py
│   ├── ai_service.py
│   ├── models.py
│   ├── schema.py
│   ├── database.py
│   └── classifier.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md
```

---

# API Endpoints

## Process a Ticket

```http
POST /process
```

Request:

```json
{
    "from_email": "customer@example.com",
    "subject": "Refund Request",
    "message": "I want my money back."
}
```

Response:

```json
{
    "category": "Refund",
    "response": "I'm happy to help you with your refund request...",
    "status": "OPEN"
}
```

---

## Get All Tickets

```http
GET /tickets
```

---

## Get Ticket by ID

```http
GET /tickets/{id}
```

---

## Update Ticket Status

```http
PATCH /tickets/{id}
```

---

## Delete Ticket

```http
DELETE /tickets/{id}
```

---

# Running the Project

## Clone the Repository

```bash
git clone https://github.com/BayanElshaer/AI-Customer-Support-Automation.git

cd AI_customer_support_automation
```

---

## Configure Environment Variables

Create a `.env` file:

```text
GROQ_API_KEY=your_api_key_here
```

Or use the provided `.env.example`.

---

## Run with Docker

Build and start all services:

```bash
docker compose build

docker compose up
```

---

## Access Services

FastAPI:

```text
http://localhost:8000
```

Swagger Documentation:

```text
http://localhost:8000/docs
```

n8n Editor:

```text
http://localhost:5678
```

---

# Example Usage

PowerShell:

```powershell
Invoke-RestMethod `
-Uri "http://localhost:5678/webhook-test/ticket" `
-Method POST `
-ContentType "application/json" `
-Body '{"message":"The website crashes when I log in."}'
```

Response:

```json
{
    "category": "Technical",
    "response": "Thank you for reaching out to us about the issue...",
    "status": "OPEN"
}
```

---

# Skills Demonstrated

This project showcases practical experience with:

* Python backend development
* FastAPI REST APIs
* Pydantic data validation
* SQLModel and relational databases
* Docker and Docker Compose
* Workflow automation with n8n
* Webhooks and HTTP integrations
* AI/LLM integrations
* Prompt engineering
* Environment configuration management
* Debugging distributed systems
* API testing and troubleshooting

---

# Future Improvements

The current implementation represents the Minimum Viable Product (MVP). Planned enhancements include:

### Database Improvements

* PostgreSQL support
* Alembic database migrations
* Advanced ticket filtering and searching
* Pagination support

### Workflow Automation

* Automatic ticket escalation
* Auto-resolution workflows
* SLA monitoring
* Priority assignment logic

### Integrations

* Slack notifications
* Microsoft Teams integration
* Email notifications
* CRM integrations

### Testing & Quality

* Unit tests using Pytest
* Integration testing
* Code coverage reports
* Static analysis with Ruff

### CI/CD

* GitHub Actions pipelines
* Automated Docker builds
* Automated testing on pull requests
* Continuous deployment workflows

### Security

* JWT authentication
* Role-based access control (RBAC)
* API rate limiting
* Secrets management

### Observability

* Structured logging
* Health checks
* Metrics and monitoring
* Error tracking

### Deployment

* Kubernetes support
* Cloud deployment (AWS/Azure/GCP)
* Production-ready Docker configuration

---

# Resume Highlights

**AI Customer Support Automation**

* Designed and developed an AI-powered customer support platform using FastAPI, Groq LLMs, n8n, SQLModel, and Docker.
* Automated ticket classification and professional response generation using prompt-engineered LLM workflows.
* Built REST APIs, webhooks, and workflow orchestration pipelines for end-to-end ticket processing.
* Implemented persistent ticket lifecycle management using SQLModel and SQLite.
* Containerized services with Docker Compose and environment-based configuration management.
* Reduced manual ticket triage effort through intelligent automation.

---

# License

This project is released under the MIT License.
