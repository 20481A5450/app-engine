import firebase_admin
from fastapi import FastAPI,HTTPException

app = FastAPI()

@app.get("/")
def root():
    return {"Api is up and running": "True"}
