from pydantic import BaseModel
from typing import Optional
from datetime import datetime
class ConcatenadoSelectModel(BaseModel):
    id: Optional[int]
    descripcion: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
class ConcatenadoCreateModel(BaseModel):
    descripcion: str

class LastID(BaseModel):
    id: int

