from pydantic import BaseModel, Field, field_validator
from backend.validators import FieldValidator


class SStudent(BaseModel):
    class Config:
        from_attributes = True

    id: int
    fio: str = Field(..., min_length=3, max_length=100, description='ФИО студента')
    post: str = Field(..., min_length=3, max_length=50, description='Должность, от 3 до 50 символов')
    level_skill: int = Field(..., gt=0, description='Уровень владения (ID навыка)')
    speciality: str = Field(..., min_length=3, max_length=200, description='Специальность, от 3 до 200 символов')
    course: int = Field(..., ge=1, le=6, description='Номер курса (1-6)')
    ability: str = Field(..., min_length=3, max_length=500, description="Описание умений, от 3 до 500 символов")
    subscribe: bool = Field(..., description='Подписан ли на рекомендации вакансий')
    code_word: str = Field(..., max_length=50, description='Фраза для рекомендаций вакансий')


class SStudentAdd(BaseModel):
    fio: str = Field(..., min_length=3, max_length=100, description='ФИО студента')
    post: str = Field(..., min_length=3, max_length=50, description='Должность, от 3 до 50 символов')
    level_skill: int = Field(..., gt=0, description='Уровень владения (ID навыка)')
    speciality: str = Field(..., min_length=3, max_length=200, description='Специальность, от 3 до 200 символов')
    course: int = Field(..., ge=1, le=6, description='Номер курса (1-6)')
    ability: str = Field(..., min_length=3, max_length=500, description="Описание умений, от 3 до 500 символов")
    subscribe: bool = Field(default=False, description='Подписан ли на рекомендации вакансий')
    code_word: str = Field(default='', max_length=50, description='Фраза для рекомендаций вакансий')
    
    @field_validator('fio', mode='before')
    @classmethod
    def validate_fio(cls, v):
        return FieldValidator.validate_fio(v)
    
    @field_validator('post', mode='before')
    @classmethod
    def validate_post(cls, v):
        return FieldValidator.validate_string(v, min_length=3, max_length=50, field_name='Должность')
    
    @field_validator('speciality', mode='before')
    @classmethod
    def validate_speciality(cls, v):
        return FieldValidator.validate_string(v, min_length=3, max_length=200, field_name='Специальность')
    
    @field_validator('course', mode='before')
    @classmethod
    def validate_course(cls, v):
        return FieldValidator.validate_course(v)
    
    @field_validator('ability', mode='before')
    @classmethod
    def validate_ability(cls, v):
        return FieldValidator.validate_string(v, min_length=3, max_length=500, field_name='Описание умений')


class SStudentUpd(BaseModel):
    fio: str | None = Field(None, min_length=3, max_length=100, description='ФИО студента')
    post: str | None = Field(None, min_length=3, max_length=50, description='Должность, от 3 до 50 символов')
    level_skill: int | None = Field(None, gt=0, description='Уровень владения (ID навыка)')
    speciality: str | None = Field(None, min_length=3, max_length=200, description='Специальность, от 3 до 200 символов')
    course: int | None = Field(None, ge=1, le=6, description='Номер курса (1-6)')
    ability: str | None = Field(None, min_length=3, max_length=500, description="Описание умений, от 3 до 500 символов")
    subscribe: bool | None = Field(None, description='Подписан ли на рекомендации вакансий')
    code_word: str | None = Field(None, max_length=50, description='Фраза для рекомендаций вакансий')
    
    @field_validator('fio', mode='before')
    @classmethod
    def validate_fio(cls, v):
        if v is not None:
            return FieldValidator.validate_fio(v)
        return v
    
    @field_validator('post', mode='before')
    @classmethod
    def validate_post(cls, v):
        if v is not None:
            return FieldValidator.validate_string(v, min_length=3, max_length=50, field_name='Должность')
        return v
    
    @field_validator('speciality', mode='before')
    @classmethod
    def validate_speciality(cls, v):
        if v is not None:
            return FieldValidator.validate_string(v, min_length=3, max_length=200, field_name='Специальность')
        return v
    
    @field_validator('course', mode='before')
    @classmethod
    def validate_course(cls, v):
        if v is not None:
            return FieldValidator.validate_course(v)
        return v
    
    @field_validator('ability', mode='before')
    @classmethod
    def validate_ability(cls, v):
        if v is not None:
            return FieldValidator.validate_string(v, min_length=3, max_length=500, field_name='Описание умений')
        return v