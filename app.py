from fastapi import FastAPI
from pydantic import BaseModel
from model import generate_recommendation

app = FastAPI()

class FashionRequest(BaseModel):
    gender: str
    occasion: str
    season: str
    color_preference: str

@app.get("/")
def home():
    return {"message": "Fashion AI API running"}

@app.post("/recommend")
def recommend(req: FashionRequest):
    result = generate_recommendation(
        req.gender,
        req.occasion,
        req.season,
        req.color_preference
    )
    
    return {"recommendation": result}