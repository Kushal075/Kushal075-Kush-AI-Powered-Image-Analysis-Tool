from fastapi import FastAPI
from processing.api import medical_routes, crop_routes

app = FastAPI()

# ...existing code...

app.include_router(medical_routes.router, prefix="/api")
app.include_router(crop_routes.router, prefix="/api")

# ...existing code...
