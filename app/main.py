from fastapi import FastAPI, File, UploadFile
import pandas as pd

app = FastAPI()

@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    file.file.close()
    return {"filename": file.filename}
