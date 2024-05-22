from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PlanMovimientoSelectModel(BaseModel):
    id: Optional[int]
    id_movimiento: int
    fecha: datetime
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class PlanMovimientoCreateModel(BaseModel):
    id_movimiento: int
    fecha: datetime
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class LastID(BaseModel):
    id: int