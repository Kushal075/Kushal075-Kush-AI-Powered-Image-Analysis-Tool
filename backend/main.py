from fastapi import FastAPI
from processing.api import medical_routes, crop_routes

app = FastAPI()

app.include_router(medical_routes.router)
app.include_router(crop_routes.router)

@app.get("/")
def root():
    return {"message": "AI Image Analysis Tool is running!"}
