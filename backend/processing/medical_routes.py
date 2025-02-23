import os
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from backend.models.medical_model import predict_brain_tumor

medical_bp = Blueprint("medical", __name__)

# Directory to store uploaded images
UPLOAD_FOLDER = "backend/uploads/medical"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

def allowed_file(filename):
    """Check if file extension is allowed."""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@medical_bp.route("/predict/brain_tumor", methods=["POST"])
def upload_image():
    """
    API Endpoint to handle image uploads for brain tumor prediction.
    - Accepts an image file
    - Returns AI prediction with confidence score
    """
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)

        # Perform AI prediction
        result = predict_brain_tumor(filepath)

        # Remove the uploaded file after prediction (optional)
        os.remove(filepath)

        return jsonify({
            "prediction": result["prediction"],
            "confidence": f"{result['confidence']:.2f}%"
        })

    return jsonify({"error": "Invalid file type"}), 400
