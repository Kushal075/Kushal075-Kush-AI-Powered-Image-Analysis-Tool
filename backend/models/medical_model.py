import tensorflow as tf
import numpy as np
import cv2
import os

# Load the pre-trained model (adjust filename if needed)
MODEL_PATH = os.path.join(os.path.dirname(__file__), "brain_tumor_model.h5")
model = tf.keras.models.load_model(MODEL_PATH)

# Class labels (adjust if needed)
CLASS_LABELS = ["No Tumor", "Tumor Detected"]

def preprocess_image(image_path):
    """
    Preprocesses an image for the brain tumor model.
    - Resizes to (224, 224) (adjust if needed)
    - Converts to array and normalizes
    """
    img = cv2.imread(image_path)
    img = cv2.resize(img, (224, 224))  # Ensure the model input size is correct
    img = img / 255.0  # Normalize pixel values
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    return img

def predict_brain_tumor(image_path):
    """
    Predicts whether the image contains a brain tumor.
    Returns:
    - Predicted class (Tumor / No Tumor)
    - Confidence score
    """
    img = preprocess_image(image_path)
    prediction = model.predict(img)[0]  # Get the first (and only) prediction
    class_idx = np.argmax(prediction)  # Get the highest probability class
    confidence = float(prediction[class_idx]) * 100  # Convert to percentage
    
    return {
        "prediction": CLASS_LABELS[class_idx],
        "confidence": confidence
    }
