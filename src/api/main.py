from fastapi import FastAPI
from src.api.routes import router

app = FastAPI(
    title="AI File Generator API",
    description="Generate files (DOCX, Excel) from natural language instructions using LLMs",
    version="0.1.0",
)

app.include_router(router)
