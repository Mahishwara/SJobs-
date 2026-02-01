from pydantic import BaseModel, Field, field_validator


class SStudent(BaseModel):
    class Config:
        from_attributes = True

    id: int
    fio: str = Field(..., min_length=3, max_length=100, description='ФИО')
    post: str = Field(..., min_length=3, max_length=50, description='Должность, от 3 до 50 символов')
    level_skill: int = Field(..., description='Уровень владения')
    speciality: str = Field(..., min_length=3, max_length=200, description='Специальность, от 3 до 200 символов')
    course:  int = Field(...,description='Номер курса')
    ability: str = Field(..., min_length=3, max_length=500, description="Описание умений, от 3 до 500 символов")
    subscribe: bool
    code_word: str = Field(..., description='Фраза по которой будут отображаться новые рекомендованные вакансии')


class SStudentAdd(BaseModel):
    fio: str = Field(..., min_length=3, max_length=100, description='ФИО')
    post: str = Field(..., min_length=3, max_length=50, description='Должность, от 3 до 50 символов')
    level_skill: int = Field(..., description='Уровень владения')
    speciality: str = Field(..., min_length=3, max_length=200, description='Специальность, от 3 до 200 символов')
    course: int = Field(..., description='Номер курса')
    ability: str = Field(..., min_length=3, max_length=500, description="Описание умений, от 3 до 500 символов")



class SStudentUpd(BaseModel):
    fio: str = Field(..., min_length=3, max_length=100, description='ФИО')
    post: str = Field(..., min_length=3, max_length=50, description='Должность, от 3 до 50 символов')
    level_skill: int = Field(..., description='Уровень владения')
    speciality: str = Field(..., min_length=3, max_length=200, description='Специальность, от 3 до 200 символов')
    course: int = Field(..., description='Номер курса')
    ability: str = Field(..., min_length=3, max_length=500, description="Описание умений, от 3 до 500 символов")
    subscribe: bool
    code_word: str = Field(..., max_length=50,
                           description='Фраза по которой будут отображаться новые рекомендованные вакансии')