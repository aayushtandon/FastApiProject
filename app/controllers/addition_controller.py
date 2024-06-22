from fastapi import APIRouter, HTTPException
from app.models.request_response_models import AdditionRequest, AdditionResponse
from app.services.addition_service import perform_addition
from app.utils.logger import logger

router = APIRouter()

@router.post("/add", response_model=AdditionResponse)
async def add_numbers(request: AdditionRequest):
    try:
        result = perform_addition(request.numbers)
        return AdditionResponse(result=result)
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
