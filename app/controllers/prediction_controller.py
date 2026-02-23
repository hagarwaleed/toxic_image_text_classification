from app.models.caption_model import generate_caption
from app.models.toxicity_model import classify_text
from app.database.db import save_prediction


def predict_from_text(text):
    label = classify_text(text)
    save_prediction("text", text, label)
    return label


def predict_from_image(image_file):
    caption = generate_caption(image_file)
    label = classify_text(caption)

    save_prediction("image", caption, label)

    return caption, label