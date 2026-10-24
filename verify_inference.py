
import json
import torch
from torchvision import transforms
from medmnist import BloodMNIST

from model import create_cnn
from inference import predicted_image

#1. load model config
with open("model_config.json","r") as f:
  config = json.load(f)

#2. create cnn architecture
model = create_cnn()

#3.load the trained checkpoint
model.load_state_dict(
    torch.load(
        config["checkpoint"],
        map_location="cpu",
        weights_only = True
    )
)

#4.load one sample  using the recorded preprocessing
assert config["preprocessing"] == "ToTensor"

dataset = BloodMNIST(
    split = "test",
    transform = transforms.ToTensor(),
    download = True
)

image, actual_label = dataset[0]

#5. predict class using imported inference function

result = predicted_image(model, image, config["class_mapping"])

print("Actual class:", config["class_mapping"][str(actual_label.item())])
print("Prediction:", result)
