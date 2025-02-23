import tensorflow as tf
import numpy as np
import cv2
import os

MODEL_PATH = r"C:/Users/KUSHAL/OneDrive/Desktop/AI-Image-Analysis-Tool/Kushal075-Kush-AI-Powered-Image-Analysis-Tool/backend/models/brain_tumor_model.h5"

# Check if model file exists before loading
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"❌ Model file not found at: {MODEL_PATH}")

model = tf.keras.models.load_model(MODEL_PATH)

# ✅ Class labels (Adjust based on your model)
CLASS_LABELS = ["No Tumor", "Tumor Detected"]

def preprocess_image(image_path):
    """
    Preprocesses an image for the brain tumor model.
    - Converts grayscale images to 3 channels
    - Resizes to (224, 224) (adjust if needed)
    - Normalizes pixel values
    """
    img = cv2.imread(image_path)

    if img is None:
        raise ValueError(f"❌ Error: Unable to read image at {image_path}")

    img = cv2.resize(img, (224, 224))  # ✅ Resize to model input size
    
    # ✅ Ensure it has 3 channels (convert grayscale to RGB)
    if len(img.shape) == 2:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

    img = img / 255.0  # ✅ Normalize pixel values to [0,1]
    img = np.expand_dims(img, axis=0)  # ✅ Add batch dimension
    return img

def predict_brain_tumor(image_path):
    """
    Predicts whether the image contains a brain tumor.
    Returns:
    - Predicted class ("No Tumor" / "Tumor Detected")
    - Confidence score (%)
    """
    img = preprocess_image(image_path)
    prediction = model.predict(img)[0]  # ✅ Get prediction

    if len(prediction) == 1:
        confidence = float(prediction[0]) * 100
        class_idx = 1 if confidence > 50 else 0  # ✅ Assume threshold-based classification
    else:
        class_idx = np.argmax(prediction)  # ✅ Get class with highest probability
        confidence = float(prediction[class_idx]) * 100

    return {
        "prediction": CLASS_LABELS[class_idx],
        "confidence": confidence
    }
