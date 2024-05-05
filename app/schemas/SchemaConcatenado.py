from pydantic import BaseModel
from typing import Optional
from datetime import datetime
class ConcatenadoSelectModel(BaseModel):
    id: Optional[int]
    id_plan_movimiento: int
    descripcion: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
class ConcatenadoCreateModel(BaseModel):
    id_plan_movimiento: int
    descripcion: str


