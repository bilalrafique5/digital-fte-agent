from fastapi import APIRouter, HTTPException
from models.schemas import ContentRequest, ContentResponse
from services.workflow import run_content_pipeline

router = APIRouter()

@router.post("/generate", response_model=ContentResponse)
async def generate_content(request: ContentRequest):
    try:
        result = run_content_pipeline(request.topic, request.platforms)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))