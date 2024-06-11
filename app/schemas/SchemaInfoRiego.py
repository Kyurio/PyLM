from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class InfoRiegoSelectModel(BaseModel):
    id: Optional[int]
    id_concatenado: int
    id_loma: int
    fecha_inicio: Optional[datetime] = None
    fecha_termino: Optional[datetime] = None
    largo: float
    ancho: float
    status: str
    volumen: float
    altura: float
    area: float
    tonelaje: float
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class InfoRiegoCreateModel(BaseModel):
    id_concatenado: int
    id_loma: int
    fecha_inicio: Optional[datetime] = None
    fecha_termino: Optional[datetime] = None
    largo: float
    ancho: float
    status: str
    volumen: float
    altura: float
    area: float
    tonelaje: float

class LastID(BaseModel):
    id: int