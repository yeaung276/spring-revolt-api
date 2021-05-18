from fastapi import APIRouter,status,HTTPException,UploadFile,File
from sqlalchemy.orm import Session
import cloudinary.uploader as uploader



fileRouter = APIRouter(
    prefix='/file',
    tags=['file']
)

@fileRouter.post('/upload')
async def uploadFile(file:UploadFile=File(...)):
    result = uploader.upload(file.file)
    return result.get('url')