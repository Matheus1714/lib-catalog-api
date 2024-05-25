from fastapi import FastAPI
from .routers import doc

app = FastAPI()

app.include_router(doc.router)

