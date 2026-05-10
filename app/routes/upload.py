from fastapi import APIRouter, Depends, UploadFile
import os

router = APIRouter(prefix="/extract", tags=["extract"])

@router.post("/")
async def extract(file: UploadFile()):
    os.makedirs("/uploads",exist_ok=True)
    file_path=f"uploads/{file.filename}"
    content= await file.read()
    with open(file_path,"wb") as f:
        f.write(content)
    return {
        "filename": file.filename,
        "saved_path": file_path
    }
    