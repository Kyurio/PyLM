from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class DiasRiegoSelectModel(BaseModel):
    id: Optional[int]
    id_tipo_riego: int
    id_concatenado: int
    id_loma: int
    fecha: Optional[datetime] = None
    horas_de_riego: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class DiasRiegoCreateModel(BaseModel):
    id_tipo_riego: int
    id_concatenado: int
    id_loma: int
    fecha: Optional[datetime] = None
    horas_de_riego: Optional[int]

class LastID(BaseModel):
    id: int