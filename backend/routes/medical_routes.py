from fastapi import APIRouter, File, UploadFile
from models.medical_model import MedicalModel

router = APIRouter()
model = MedicalModel("path_to_medical_model.pth")

@router.post("/medical/predict")
async def predict_medical_image(file: UploadFile = File(...)):
    file_location = f"static/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    prediction = model.predict(file_location)
    return {"prediction": prediction}
