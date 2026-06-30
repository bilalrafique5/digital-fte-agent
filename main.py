from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from api.routes import router
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    )

app.include_router(router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Digitial FTE AI Content Agent is running successfully"}
