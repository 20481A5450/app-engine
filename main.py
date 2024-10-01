from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"Api is up and running": "True"}
