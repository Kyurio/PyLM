from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TipoRiegoSelectModel(BaseModel):
    id: Optional[int]
    nombre: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class TipoRiegoCreateModel(BaseModel):

    nombre: str

class LastID(BaseModel):
    id: int
