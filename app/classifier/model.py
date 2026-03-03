from pathlib import Path
import tensorflow as tf


def load_labels(labels_path: str) -> list[str]:
    p = Path(labels_path)
    if not p.exists():
        raise FileNotFoundError(
            f"labels file not found: {labels_path}. "
            "Create model/labels.txt with one class name per line."
        )

    labels = [line.strip() for line in p.read_text(encoding="utf-8").splitlines()]
    labels = [x for x in labels if x]
    if not labels:
        raise ValueError("labels.txt is empty")
    return labels


def load_model(model_path: str) -> tf.keras.Model:
    p = Path(model_path)
    if not p.exists():
        raise FileNotFoundError(
            f"model file not found: {model_path}. "
            "Put your trained Keras model into model/model.keras"
        )
    return tf.keras.models.load_model(model_path)
