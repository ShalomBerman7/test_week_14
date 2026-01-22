from fastapi import FastAPI, File, UploadFile
import pandas as pd
import uvicorn
from models import cut_categorize

app = FastAPI()

@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    file.file.close()
    cut_categorize(df)
    return {"filename": file.filename}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
