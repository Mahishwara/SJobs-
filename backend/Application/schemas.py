from pydantic import BaseModel, Field, field_validator
import datetime


class SApplication(BaseModel):
    class Config:
        from_attributes = True

    id: int
    id_student: int = Field(..., description='Ссылка на студента')
    id_vacancy: int = Field(..., description='Ссылка на вакансию')
    date: datetime.date = Field(..., description='Дата подачи заявки, формата ДД.ММ.ГГГГ')
    id_status: int = Field(..., description='Ссылка на статус')



class SApplicationAdd(BaseModel):
    id_student: int = Field(..., description='Ссылка на студента')
    id_vacancy: int = Field(..., description='Ссылка на вакансию')



class SApplicationUpdStatus(BaseModel):
    id_status: int = Field(..., description='Ссылка на новый статус')