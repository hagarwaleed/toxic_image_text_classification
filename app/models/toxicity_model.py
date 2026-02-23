import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

MODEL_PATH = "model_folder/distilbert-toxic-full"

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)
model.to(device)
model.eval()


def classify_text(text):
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=256
    ).to(device)

    with torch.no_grad():
        outputs = model(**inputs)

    predicted_class_id = outputs.logits.argmax(dim=-1).item()
    predicted_label = model.config.id2label[predicted_class_id]

    return predicted_label