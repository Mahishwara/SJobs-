from pydantic import BaseModel, Field


class SMessage(BaseModel):
    class Config:
        from_attributes = True

    id: int
    id_student: int = Field(..., description="Уникальный код получателя")
    id_vacancy: int = Field(..., description="Уникальный код отправителя")
    description: str = Field(..., max_length=100, description="Сообщение")
    path_type: int = Field(..., description="Путь сообщения: 1 = студент-вакансия; 2 = вакансия-студент")


class SMessageAdd(BaseModel):
    id_student: int = Field(..., description="Уникальный код получателя")
    id_vacancy: int = Field(..., description="Уникальный код отправителя")
    description: str = Field(..., min_length=10, max_length=100, description="Сообщение")
    path_type: int = Field(..., description="Путь сообщения: 1 = студент-вакансия; 2 = вакансия-студент")