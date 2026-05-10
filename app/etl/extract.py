from fastapi import UploadFile
import os
import pymupdf as fitz
import pytesseract as pt
from PIL import Image

async def save_upload_file(file: UploadFile):   #this is async because its a i/o heavy task
    os.makedirs("uploads",exist_ok=True)
    file_path=f"uploads/{file.filename}"
    content= await file.read()
    with open(file_path,"wb") as f:
        f.write(content)
    return file_path
    
def extract_pdf_text(file_path): #not async because its a cpu heavy task
    try:
        doc=fitz.open(file_path)
    except Exception as e:
        raise e
    pages=[]
    for page in doc:
        content=page.get_text()
        if len(content)<10:
            pixmap=page.get_pixmap()
            img=Image.frombytes("RGB",(pixmap.width,pixmap.height), pixmap.tobytes())
            content=pt.image_to_string(img)

        pages.append(content)
    raw_text="\n".join(pages)
    return raw_text

def detect_doc_type(raw_text:str):
    
    
        