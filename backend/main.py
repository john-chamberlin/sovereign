from fastapi import FastAPI
from routes import workflows, executions, integrations


app = FastAPI(title='Sovereign API')


app.include_router(workflows.router)
app.include_router(executions.router)
app.include_router(integrations.router)