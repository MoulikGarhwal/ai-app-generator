from fastapi import FastAPI
from pydantic import BaseModel

from backend.nintent import extract_intent
from backend.odatabase import generate_database
from backend.papi_schema import generate_api_schema
from backend.validator import validate_output
from backend.w_repair import repair_output
from backend.x_auth import generate_auth
from backend.y_metrics import (
    start_timer,
    end_timer,
    update_metrics,
    get_metrics
)

from backend.y_nassumptions import generate_assumptions
app = FastAPI()


class PromptRequest(BaseModel):
    prompt: str


@app.get("/")
def home():
    return {"message": "Backend Running"}


@app.post("/generate")
def generate_app(data: PromptRequest):
    start_time = start_timer()

    # Intent Extraction
    intent = extract_intent(data.prompt)
    assumptions = generate_assumptions(data.prompt)

    # Page Generation
    pages = []

    if intent["app_type"] == "crm":
        pages = ["login", "dashboard", "contacts"]

    elif intent["app_type"] == "ecommerce":
        pages = ["home", "products", "cart"]

    else:
        pages = ["home"]

    # Database Schema
    database = generate_database(intent["app_type"])

    # API Schema
    api_schema = generate_api_schema(intent["app_type"])

    # Auth System
    auth = generate_auth(intent["app_type"])

    # Final Output
    final_output = {
        "app_name": "AI Generated App",
        "intent": intent,
        "pages": pages,
        "database": database,
        "api_schema": api_schema,
        "auth": auth
    }

    # Validation
    validation = validate_output(final_output)

    final_output["validation"] = validation

    # Auto Repair
    if validation["valid"] == False:
        final_output = repair_output(final_output)

    # Update metrics
    update_metrics(success=validation["valid"])

    # Calculate latency
    latency = end_timer(start_time)

    # Get final metrics
    metrics = get_metrics(latency)

    latency = end_timer(start_time)

    update_metrics(success=True)

    metrics = get_metrics(latency)

    final_output["metrics"] = metrics

    final_output["assumptions"] = assumptions

    return final_output