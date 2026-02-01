from pydantic import BaseModel, Field, field_validator
from datetime import datetime, date, time


class SInterview(BaseModel):
    class Config:
        from_attributes = True

    id: int
    id_student: int = Field(..., description="Уникальный код студента")
    id_vacancy: int = Field(..., description="Уникальный код вакансии")
    date_start: date = Field(..., description="Дата собеседования по вакансии")
    time_start: time = Field(..., description='Время собеседования по вакансии')


class SInterviewAdd(BaseModel):
    id_student: int = Field(..., description="Уникальный код студента")
    id_vacancy: int = Field(..., description="Уникальный код вакансии")
    date_start: str = Field(..., description="Дата собеседования по вакансии, в формате ГГГГ-ММ-ДД")
    time_start: str = Field(..., description='Время собеседования, в формате ЧЧ:ММ')

    @field_validator('date_start')
    @classmethod
    def validate_date(cls, values: str) -> date:
        validate_date = datetime.strptime(values, '%Y-%m-%d')

        if validate_date and validate_date > datetime.today():
            return validate_date.date()
        raise ValueError('Дата должна быть в формате ГГГГ-ММ-ДД и быть позднее сегодняшнего дня')


    @field_validator('time_start')
    @classmethod
    def validate_time(cls, values: str) -> date:
        validate_date = datetime.strptime(values, '%H:%M')

        if validate_date and validate_date:
            return validate_date.time()
        raise ValueError('Время должно быть в формате ЧЧ:MM и быть позднее сегодняшнего дня')


class SInterviewUpd(BaseModel):
    date_start: str = Field(..., description="Дата собеседования по вакансии, в формате ГГГГ-ММ-ДД")
    time_start: str = Field(..., description='Время собеседования, в формате ЧЧ:ММ')

    @field_validator('date_start')
    @classmethod
    def validate_date(cls, values: str) -> date:
        validate_date = datetime.strptime(values, '%Y-%m-%d')

        if validate_date and validate_date > datetime.today():
            return validate_date.date()
        raise ValueError('Дата должна быть в формате ГГГГ-ММ-ДД и быть позднее сегодняшнего дня')

    @field_validator('time_start')
    @classmethod
    def validate_time(cls, values: str) -> date:
        validate_date = datetime.strptime(values, '%H:%M')

        if validate_date and validate_date:
            return validate_date.time()
        raise ValueError('Время должно быть в формате ЧЧ:MM')