from pydantic import BaseModel, Field


class SFeedback(BaseModel):
    class Config:
        from_attributes = True

    id: int
    id_to: int = Field(..., description="Уникальный код получателя")
    id_from: int = Field(..., description="Уникальный код отправителя")
    rate: int = Field(..., description='Показатель рейтинга')
    description: str = Field(..., max_length=200, description="Отзыв работодателя о студенте")
    path: int = Field(..., description='0 = студент- работодатель; 1 = студент-вакансия; 2 = работодатель студент')


class SFeedbackAdd(BaseModel):
    id_to: int = Field(..., description="Уникальный код получателя")
    id_from: int = Field(..., description="Уникальный код отправителя")
    rate: int = Field(..., description='Показатель рейтинга')
    description: str = Field(..., max_length=200, description="Отзыв работодателя о студенте")
    path: int = Field(..., description='0 = студент- работодатель; 1 = студент-вакансия; 2 = работодатель студент')

class SFeedbackUpd(BaseModel):
    rate: int = Field(..., description='Показатель рейтинга')
    description: str = Field(..., max_length=200, description="Отзыв работодателя о студенте")