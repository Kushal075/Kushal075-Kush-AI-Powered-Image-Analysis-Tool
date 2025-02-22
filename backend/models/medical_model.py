import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image

class MedicalModel:
    def __init__(self, device=None):
        # Use GPU if available, otherwise fallback to CPU
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")

        # Load a pre-trained model (ResNet18)
        self.model = models.resnet18(pretrained=True).to(self.device)
        self.model.eval()  # Set model to evaluation mode

        # Define the transformation for input images
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])

        # Sample labels (modify as needed)
        self.class_labels = ["Class 0", "Class 1", "Class 2"]  # Example labels

    def predict(self, image_path):
        """
        Predict the class of the input image.
        :param image_path: Path to the image file
        :return: Predicted class label
        """
        try:
            # Load and transform the image
            image = Image.open(image_path).convert("RGB")
            image = self.transform(image).unsqueeze(0).to(self.device)

            # Get predictions
            with torch.no_grad():
                output = self.model(image)
            _, predicted = torch.max(output, 1)

            # Return class label if available, else return index
            return self.class_labels[predicted.item()] if predicted.item() < len(self.class_labels) else f"Class {predicted.item()}"

        except Exception as e:
            print(f"Error processing image: {e}")
            return None
