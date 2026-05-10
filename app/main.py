# app/main.py

from fastapi import FastAPI
from app.storage import Base, engine

app = FastAPI()


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"status": "ok"}