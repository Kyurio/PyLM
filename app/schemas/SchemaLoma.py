from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class LomaSelectModel(BaseModel):
    id: Optional[int]
    nombre: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class LomaCreateModel(BaseModel):

    nombre: str

class LastID(BaseModel):
    id: int
