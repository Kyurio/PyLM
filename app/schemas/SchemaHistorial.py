from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class HistorialSelectModel(BaseModel):
    id: Optional[int]
    usuario_id: int
    tabla_afectada: str
    accion: str
    fecha_hora: Optional[datetime] = None
    created_at: Optional[datetime] = None


class HistorialCreateModel(BaseModel):
    id: Optional[int]
    usuario_id: int
    tabla_afectada: str
    accion: str
    fecha_hora: Optional[datetime] = None
    created_at: Optional[datetime] = None