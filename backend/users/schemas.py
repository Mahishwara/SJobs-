import re

from pydantic import BaseModel, EmailStr, Field, field_validator


class SUser(BaseModel):
    class Config:
        from_attributes = True
    email: EmailStr = Field(..., description="Электронная почта")
    phone_number: str = Field(..., description='Номер телефона')


class SUserRegister(BaseModel):
    email: EmailStr = Field(..., description="Электронная почта")
    password: str = Field(..., min_length=5, max_length=50, description="Пароль, от 5 до 50 знаков")
    phone_number: str = Field(..., description="Номер телефона в международном формате, начинающийся с '+'")


    @field_validator("phone_number")
    @classmethod
    def validate_phone_number(cls, values: str) -> str:
        if not re.match(r'^\+\d{11}$', values):
            raise ValueError('Номер телефона должен начинаться с "+" и содержать 11 цифр')
        return values


class SUserAuth(BaseModel):
    email: EmailStr = Field(..., description="Электронная почта")
    password: str = Field(..., min_length=5, max_length=50, description="Пароль, от 5 до 50 знаков")


class SToken(BaseModel):
    token: str = Field()