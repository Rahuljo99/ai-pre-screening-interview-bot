from fastapi import APIRouter, File, UploadFile
from backend.app.services.parser import resume_parser
from backend.app.services.extractor import resume_extractor
router = APIRouter()

@router.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        return {"error": "Invalid file type. Please upload a PDF file."}
        
    file_bytes = await file.read()
    
    content = resume_parser(file_bytes)
    extracted_data = await resume_extractor(content)
    return {"filename": file.filename,"Structured data": extracted_data, "status": "uploaded and extracted successfully"}