import uuid

import uvicorn
from fastapi import BackgroundTasks, FastAPI, UploadFile

from nb4chat.s3 import Bucket, s3_client

app = FastAPI()


def process_ocr_task(file_name: str):
    s3_client.download_file(Bucket.RAW, file_name, f"/tmp/{file_name}")

    text_content = "example..."

    result_key = file_name.replace(".pdf", ".txt")
    s3_client.put_object(Bucket=Bucket.OCRED, Key=result_key, Body=text_content.encode("utf-8"))
    print(f"ocred:{result_key}")


@app.post("/upload")
def upload_pdf(file: UploadFile, background_tasks: BackgroundTasks):
    file_id = f"{uuid.uuid4()}-{file.filename}"

    s3_client.upload_fileobj(file.file, Bucket.RAW, file_id)

    background_tasks.add_task(process_ocr_task, file_id)

    return {"status": "uploaded", "file_id": file_id, "message": "ocring..."}


if __name__ == "__main__":
    uvicorn.run("app:app", port=8000, log_level="info", reload=True)
