from PIL import Image
import torch
from torchvision import models, transforms

model = models.resnet18(pretrained=True)
model.fc = torch.nn.Linear(model.fc.in_features, 3)
model.load_state_dict(torch.load("models/trend_classifier.pth"))
model.eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

def analyze_uploaded_chart(file):
    image = Image.open(file).convert('RGB')
    input_tensor = transform(image).unsqueeze(0)
    with torch.no_grad():
        outputs = model(input_tensor)
        probs = torch.nn.functional.softmax(outputs[0], dim=0)
        classes = ['Uptrend', 'Downtrend', 'Sideways']
        prediction = classes[probs.argmax()]
        confidence = probs.max().item()
    return {"trend": prediction, "confidence": round(confidence, 2)}