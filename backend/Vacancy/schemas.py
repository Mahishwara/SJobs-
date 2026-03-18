from pydantic import BaseModel, Field, field_validator
from datetime import datetime, date
from backend.validators import FieldValidator, ValidationRules


class SVacancy(BaseModel):
    class Config:
        from_attributes = True

    id: int
    post: str = Field(..., min_length=1, max_length=50, description='Наименование вакансии')
    description: str = Field(..., max_length=500, description='Дополнительная информация о вакансии')
    date_begin: date = Field(..., description='Дата начала стажировки')
    date_end: date = Field(..., description='Дата окончания стажировки')
    level_skill: int = Field(..., gt=0, description='Требуемый уровень навыка (ID)')
    salary: int = Field(..., ge=0, le=1000000, description='Зарплата (в рублях)')
    id_employer: int = Field(..., gt=0, description='Идентификатор работодателя')
    is_active: bool = Field(..., description='Активна ли вакансия')


class SVacancyAdd(BaseModel):
    post: str = Field(..., min_length=1, max_length=50, description='Наименование вакансии')
    description: str = Field(..., min_length=3, max_length=500, description='Дополнительная информация о вакансии')
    date_begin: str = Field(..., description='Дата начала стажировки, в формате ГГГГ-ММ-ДД')
    date_end: str = Field(..., description='Дата окончания стажировки, в формате ГГГГ-ММ-ДД')
    level_skill: int = Field(..., gt=0, description='Требуемый уровень навыка (ID)')
    salary: int = Field(..., ge=0, le=1000000, description='Зарплата (в рублях)')
    id_employer: int = Field(..., gt=0, description='Идентификатор работодателя')

    @field_validator('post', mode='before')
    @classmethod
    def validate_post(cls, v):
        return FieldValidator.validate_string(v, min_length=1, max_length=50, field_name='Должность')
    
    @field_validator('description', mode='before')
    @classmethod
    def validate_description(cls, v):
        return FieldValidator.validate_string(v, min_length=3, max_length=500, field_name='Описание')
    
    @field_validator('salary', mode='before')
    @classmethod
    def validate_salary(cls, v):
        return FieldValidator.validate_salary(v)
    
    @field_validator('date_begin', mode='before')
    @classmethod
    def validate_date_begin(cls, v):
        return FieldValidator.validate_date(v, field_name='Дата начала', future_required=True)
    
    @field_validator('date_end', mode='before')
    @classmethod
    def validate_date_end(cls, v):
        return FieldValidator.validate_date(v, field_name='Дата окончания', future_required=True)
    
    @field_validator('date_end', mode='after')
    @classmethod
    def validate_date_range(cls, v, info):
        if 'date_begin' in info.data:
            date_begin = info.data['date_begin']
            if date_begin and date_begin >= v:
                raise ValueError('Дата окончания должна быть позже даты начала')
        return v


class SVacancyUpd(BaseModel):
    post: str | None = Field(None, min_length=1, max_length=50, description='Новое наименование вакансии')
    description: str | None = Field(None, min_length=3, max_length=500, description='Новое описание вакансии')
    date_begin: str | None = Field(None, description='Дата начала стажировки, в формате ГГГГ-ММ-ДД')
    date_end: str | None = Field(None, description='Дата окончания стажировки, в формате ГГГГ-ММ-ДД')
    level_skill: int | None = Field(None, gt=0, description='Новый уровень навыка (ID)')
    salary: int | None = Field(None, ge=0, le=1000000, description='Новая зарплата (в рублях)')
    id_employer: int | None = Field(None, gt=0, description='Идентификатор работодателя')

    @field_validator('post', mode='before')
    @classmethod
    def validate_post(cls, v):
        if v is not None:
            return FieldValidator.validate_string(v, min_length=1, max_length=50, field_name='Должность')
        return v
    
    @field_validator('description', mode='before')
    @classmethod
    def validate_description(cls, v):
        if v is not None:
            return FieldValidator.validate_string(v, min_length=3, max_length=500, field_name='Описание')
        return v
    
    @field_validator('salary', mode='before')
    @classmethod
    def validate_salary(cls, v):
        if v is not None:
            return FieldValidator.validate_salary(v)
        return v
    
    @field_validator('date_begin', mode='before')
    @classmethod
    def validate_date_begin(cls, v):
        if v is not None:
            return FieldValidator.validate_date(v, field_name='Дата начала', future_required=True)
        return v
    
    @field_validator('date_end', mode='before')
    @classmethod
    def validate_date_end(cls, v):
        if v is not None:
            return FieldValidator.validate_date(v, field_name='Дата окончания', future_required=True)
        return v
    
    @field_validator('date_end', mode='after')
    @classmethod
    def validate_date_range(cls, v, info):
        if v is not None and 'date_begin' in info.data:
            date_begin = info.data.get('date_begin')
            if date_begin and date_begin >= v:
                raise ValueError('Дата окончания должна быть позже даты начала')
        return v


class SVacancyUpdActive(BaseModel):
    is_active: bool = Field(..., description='Активна ли вакансия')