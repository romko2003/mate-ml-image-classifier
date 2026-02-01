from io import BytesIO

import numpy as np
import tensorflow as tf
from PIL import Image


IMG_SIZE = (224, 224)


def preprocess(image_bytes: bytes) -> np.ndarray:
    """
    Convert raw image bytes -> preprocessed tensor for MobileNetV2.
    Returns shape (1, 224, 224, 3)
    """
    img = Image.open(BytesIO(image_bytes)).convert("RGB")
    img = img.resize(IMG_SIZE)
    arr = np.array(img, dtype=np.float32)
    arr = np.expand_dims(arr, axis=0)
    arr = tf.keras.applications.mobilenet_v2.preprocess_input(arr)
    return arr


def predict(model: tf.keras.Model, labels: list[str], image_bytes: bytes) -> dict:
    x = preprocess(image_bytes)
    probs = model.predict(x, verbose=0)[0]  # (num_classes,)

    idx = int(np.argmax(probs))
    return {
        "class": labels[idx],
        "confidence": float(probs[idx]),
        "probs": {labels[i]: float(probs[i]) for i in range(len(labels))},
    }
