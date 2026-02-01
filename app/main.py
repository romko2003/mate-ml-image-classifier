from pathlib import Path

from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.classifier.model import load_model, load_labels
from app.classifier.predict import predict


BASE_DIR = Path(__file__).resolve().parent          # .../app
PROJECT_ROOT = BASE_DIR.parent                      # .../repo root

TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"

MODEL_PATH = PROJECT_ROOT / "model" / "model.keras"
LABELS_PATH = PROJECT_ROOT / "model" / "labels.txt"

app = FastAPI(title="Cats vs Dogs Classifier (Keras)")

templates = Jinja2Templates(directory=str(TEMPLATES_DIR))
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

# Load model once at startup
model = load_model(str(MODEL_PATH))
labels = load_labels(str(LABELS_PATH))


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict", response_class=HTMLResponse)
async def do_predict(request: Request, file: UploadFile = File(...)):
    image_bytes = await file.read()
    result = predict(model=model, labels=labels, image_bytes=image_bytes)

    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "filename": file.filename,
            "result": result,
        },
    )
