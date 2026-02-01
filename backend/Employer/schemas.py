from pydantic import BaseModel, Field, field_validator
import re

class SEmployer(BaseModel):
    class Config:
        from_attributes = True
    id: int
    name: str = Field(..., min_length=3, max_length=100, description="Полное имя, от 3 до 50 символов")
    organization: str = Field(...,min_length=3, max_length=100, description='Наименование организации')
    description: str = Field(..., description='Дополнительная информация')
    user_id: int




class SEmployerAdd(BaseModel):
    name: str = Field(..., min_length=3, max_length=100, description="Полное имя, от 3 до 50 символов")
    organization: str = Field(..., min_length=3, max_length=100, description='Наименование организации')
    description: str = Field(..., description='Дополнительная информация')
    user_id: int


class SEmployerUpd(BaseModel):
    name: str = Field(..., min_length=3, max_length=100, description="Полное имя, от 3 до 50 символов")
    organization: str = Field(..., min_length=3, max_length=100, description='Наименование организации')
    description: str = Field(..., description='Новая дополнительная информация')