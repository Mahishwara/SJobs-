from pydantic import BaseModel, Field, field_validator
import datetime
from backend.validators import FieldValidator


class SApplication(BaseModel):
    class Config:
        from_attributes = True

    id: int
    id_student: int = Field(..., gt=0, description='ID студента, подавшего заявку')
    id_vacancy: int = Field(..., gt=0, description='ID вакансии')
    date: datetime.date = Field(..., description='Дата подачи заявки')
    id_status: int = Field(..., gt=0, description='ID статуса заявки')


class SApplicationAdd(BaseModel):
    id_student: int = Field(..., gt=0, description='ID студента')
    id_vacancy: int = Field(..., gt=0, description='ID вакансии')
    
    @field_validator('id_student', 'id_vacancy', mode='before')
    @classmethod
    def validate_id(cls, v, info):
        field_name = info.field_name
        return FieldValidator.validate_positive_int(v, field_name=f'ID {field_name}')


class SApplicationUpdStatus(BaseModel):
    id_status: int = Field(..., gt=0, description='ID нового статуса заявки')
    
    @field_validator('id_status', mode='before')
    @classmethod
    def validate_status(cls, v):
        return FieldValidator.validate_positive_int(v, field_name='ID статуса')