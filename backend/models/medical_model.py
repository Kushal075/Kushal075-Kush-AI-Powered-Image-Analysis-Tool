import torch
import torchvision.transforms as transforms
from PIL import Image

class MedicalModel:
    def __init__(self, model_path):
        self.model = torch.load(model_path)
        self.model.eval()
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])

    def predict(self, image_path):
        image = Image.open(image_path)
        image = self.transform(image).unsqueeze(0)
        with torch.no_grad():
            output = self.model(image)
        _, predicted = torch.max(output, 1)
        return predicted.item()
