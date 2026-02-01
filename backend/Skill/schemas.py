from pydantic import BaseModel, Field


class SSkill(BaseModel):
    class Config:
        from_attributes = True

    id: int
    level: str = Field(..., min_length=3, max_length=50, description="Уровень владения")



class SSkillAdd(BaseModel):
    level: str = Field(..., min_length=3, max_length=50, description="Уровень владения")



class SSkillUpd(BaseModel):
    level: str = Field(..., min_length=3, max_length=50, description="Новый уровень владения")