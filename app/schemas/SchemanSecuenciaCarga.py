from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SecuenciaDeCargaSelectModel(BaseModel):
    id: int
    concepto: int
    secuencia: int
    valor: Optional[float]
    fecha: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
