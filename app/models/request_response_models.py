from pydantic import BaseModel, conlist
from typing import List

class AdditionRequest(BaseModel):
    numbers: conlist(int, min_items=1)

class AdditionResponse(BaseModel):
    result: int
