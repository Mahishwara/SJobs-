from pydantic import BaseModel, Field, field_validator
import datetime


class SSjobs.backend.lication(BaseModel):
    class Config:
        from_attributes = True

    id: int
    id_student: int = Field(..., description='Ссылка на студента')
    id_vacancy: int = Field(..., description='Ссылка на вакансию')
    date: datetime.date = Field(..., description='Дата подачи заявки, формата ДД.ММ.ГГГГ')
    id_status: int = Field(..., description='Ссылка на статус')



class SSjobs.backend.licationAdd(BaseModel):
    id_student: int = Field(..., description='Ссылка на студента')
    id_vacancy: int = Field(..., description='Ссылка на вакансию')



class SSjobs.backend.licationUpdStatus(BaseModel):
    id_status: int = Field(..., description='Ссылка на новый статус')