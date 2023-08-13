import nemo.collections.asr as nemo_asr
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import os

app = FastAPI()

# Load the NeMo ASR model
model = nemo_asr.models.EncDecCTCModel.from_pretrained(model_name="QuartzNet15x5Base-En")

@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.post("/transcribe")
async def upload_audio(file: UploadFile):
    file_contents = await file.read()
    with open("audio.wav", "wb") as f:
        f.write(file_contents)
    print('saved audio')
    file_path = os.path.abspath("audio.wav")
    text=model.transcribe([file_path])
    ft=str(text)[2:-2]
    return ft