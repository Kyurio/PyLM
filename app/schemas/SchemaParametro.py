from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ParametroSelectModel(BaseModel):
    id: Optional[int]
    id_secuencia: int
    largo: float
    ancho: float
    ciclo_secado: int
    tasa_riego: float
    densidad: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class ParametroCreateModel(BaseModel):

    id_secuencia: int
    largo: float
    ancho: float
    ciclo_secado: int
    tasa_riego: float
    densidad: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None