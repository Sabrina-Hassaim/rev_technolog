from fastapi import FastAPI
from pymongo import MongoClient
from Musique import Musique
from typing import List
app = FastAPI()

client = MongoClient('mongodb://revision-mongodb-1:27017')
db = client["musique_db"]
col = db["musique"]

@app.get("/musique", response_model=List[Musique])
def get_musique():
    musiques = col.find()
    return list(musiques)

@app.post("/musique", response_model=Musique)
def create_musique(musique: Musique):
    musique_id = col.insert_one(musique.dict()).inserted_id
    return musique



