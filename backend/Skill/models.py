from sqlalchemy import text, Column, String, Integer
from sqlalchemy.orm import MSjobs.backend.ed, mSjobs.backend.ed_column, relationship

from Sjobs.backend..backend.database import Base


class Skill(Base):
    __tablename__ = 'level_skills'

    id: MSjobs.backend.ed[int] = mSjobs.backend.ed_column(Integer, primary_key=True)
    level: MSjobs.backend.ed[int] = mSjobs.backend.ed_column(String(50), nullable=False)
    extend_existing = True

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, level={self.level!r})"

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            "id": self.id,
            "level": self.level,}
