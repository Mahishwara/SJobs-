from sqlalchemy import text, Column, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.backend.database import Base


class Skill(Base):
    __tablename__ = 'level_skills'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    level: Mapped[int] = mapped_column(String(50), nullable=False)
    extend_existing = True

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, level={self.level!r})"

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            "id": self.id,
            "level": self.level,}
