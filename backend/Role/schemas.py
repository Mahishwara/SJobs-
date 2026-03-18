from pydantic import BaseModel, Field


class SRole(BaseModel):
    class Config:
        from_attributes = True

    id: int
    role_name: str = Field(..., description="Название роли")
    role_type: str = Field(..., description="Тип роли: 'student' или 'employer'")
    description: str | None = Field(None, description="Описание роли")


class SRoleAdd(BaseModel):
    role_name: str = Field(..., description="Название роли")
    role_type: str = Field(..., description="Тип роли: 'student' или 'employer'")
    description: str | None = Field(None, description="Описание роли")


class SRoleUpd(BaseModel):
    role_name: str | None = Field(None, description="Название роли")
    role_type: str | None = Field(None, description="Тип роли: 'student' или 'employer'")
    description: str | None = Field(None, description="Описание роли")
