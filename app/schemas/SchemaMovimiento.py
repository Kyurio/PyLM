from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MovimientoSelectModel(BaseModel):
    id: Optional[int]
    id_concepto: int
    id_secuencia: int
    valor: Optional[float]
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class MovimientoCreateModel(BaseModel):
    id_concepto: int
    id_secuencia: int
    valor: Optional[float]
