from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SecuenciaDeCargaSelectModel(BaseModel):

    secuencia: str
    concepto: str
    valor: Optional[float]
    fecha: Optional[datetime] = None
