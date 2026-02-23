import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

MODEL_NAME = "Salesforce/blip-image-captioning-large"

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

processor = BlipProcessor.from_pretrained(MODEL_NAME)
model = BlipForConditionalGeneration.from_pretrained(MODEL_NAME)
model.to(device)
model.eval()


def generate_caption(image_file):
    image = Image.open(image_file).convert("RGB")

    inputs = processor(images=image, return_tensors="pt").to(device)

    with torch.no_grad():
        output = model.generate(**inputs)

    caption = processor.decode(output[0], skip_special_tokens=True)

    return caption