from pydantic import BaseModel, Field, field_validator
from backend.validators import FieldValidator


class SEmployer(BaseModel):
    class Config:
        from_attributes = True
    
    id: int
    name: str = Field(..., min_length=3, max_length=100, description="Полное имя, от 3 до 100 символов")
    organization: str = Field(..., min_length=3, max_length=100, description='Наименование организации, от 3 до 100 символов')
    description: str = Field(..., min_length=3, max_length=500, description='Дополнительная информация об организации')
    user_id: int = Field(..., gt=0, description='ID пользователя')


class SEmployerAdd(BaseModel):
    name: str = Field(..., min_length=3, max_length=100, description="Полное имя, от 3 до 100 символов")
    organization: str = Field(..., min_length=3, max_length=100, description='Наименование организации')
    description: str = Field(..., min_length=3, max_length=500, description='Дополнительная информация об организации')
    user_id: int = Field(..., gt=0, description='ID пользователя')
    
    @field_validator('name', mode='before')
    @classmethod
    def validate_name(cls, v):
        return FieldValidator.validate_fio(v)
    
    @field_validator('organization', mode='before')
    @classmethod
    def validate_organization(cls, v):
        return FieldValidator.validate_string(v, min_length=3, max_length=100, field_name='Организация')
    
    @field_validator('description', mode='before')
    @classmethod
    def validate_description(cls, v):
        return FieldValidator.validate_string(v, min_length=3, max_length=500, field_name='Описание')


class SEmployerUpd(BaseModel):
    name: str | None = Field(None, min_length=3, max_length=100, description="Полное имя, от 3 до 100 символов")
    organization: str | None = Field(None, min_length=3, max_length=100, description='Наименование организации')
    description: str | None = Field(None, min_length=3, max_length=500, description='Дополнительная информация об организации')
    user_id: int | None = Field(None, gt=0, description='ID пользователя')
    
    @field_validator('name', mode='before')
    @classmethod
    def validate_name(cls, v):
        if v is not None:
            return FieldValidator.validate_fio(v)
        return v
    
    @field_validator('organization', mode='before')
    @classmethod
    def validate_organization(cls, v):
        if v is not None:
            return FieldValidator.validate_string(v, min_length=3, max_length=100, field_name='Организация')
        return v
    
    @field_validator('description', mode='before')
    @classmethod
    def validate_description(cls, v):
        if v is not None:
            return FieldValidator.validate_string(v, min_length=3, max_length=500, field_name='Описание')
        return v