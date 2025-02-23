from fastapi import APIRouter, File, UploadFile
from models.crop_model import CropModel

router = APIRouter()
model = CropModel("path_to_crop_model.pth")

@router.post("/crop/predict")
async def predict_crop_image(file: UploadFile = File(...)):
    file_location = f"static/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    prediction = model.predict(file_location)
    return {"prediction": prediction}
