import firebase_admin
from firebase_admin import firestore, credentials, initialize_app
from pydantic import BaseModel
from fastapi import FastAPI,HTTPException

cred = credentials.Certificate('Key.json')

firebase_admin.initialize_app(cred)

db = firestore.client()

app = FastAPI()

class CollectionRequest(BaseModel):
    collection_name: str

@app.get("/")
def root():
    return {"Api is up and running": "True"}


@app.post("/collections")
def get_collection(request: CollectionRequest):
    try:
        collection_name = request.collection_name
        docs = db.collection(collection_name).stream()
        documents = [doc.to_dict() for doc in docs]
        # print(documents)
        return {"collection_name": collection_name, "documents": documents}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))