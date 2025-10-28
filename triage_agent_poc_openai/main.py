
from fastapi import FastAPI
from triage_agent_poc.routes.decision_routes import router

app = FastAPI(title="Dynamic Decision Routing Agent with Azure AI")
app.include_router(router)

@app.get("/health")
def health_check():
    return {"status": "ok"}
