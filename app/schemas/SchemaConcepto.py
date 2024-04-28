from pydantic import BaseModel
from datetime import datetime
class ConceptoCreateModel(BaseModel):
    nombre: str
class ConceptoSelectModel(BaseModel):
    id: int
    nombre: str
    created_at: datetime
    updated_at: datetime
