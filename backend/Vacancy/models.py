from sqlalchemy import String, Integer, ForeignKey, BOOLEAN
from sqlalchemy.dialects.mysql import DATETIME, DATE
from sqlalchemy.orm import Mapped, mapped_column
from app.backend.database import Base
from datetime import datetime, date

class Vacancy(Base):
    __tablename__ = 'vacancies'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    post: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String(100), nullable=False)
    publication_date: Mapped[datetime] = mapped_column(DATETIME, nullable=True, default=datetime.now)
    date_begin: Mapped[date] = mapped_column(DATE, nullable=True)
    date_end: Mapped[date] = mapped_column(DATE, nullable=True)
    level_skill: Mapped[int] = mapped_column(ForeignKey('level_skills.id'), nullable=False)
    salary: Mapped[int] = mapped_column(Integer, nullable=False)
    id_employer: Mapped[int] = mapped_column(ForeignKey('employers.id'), nullable=False)
    is_active: Mapped[bool] = mapped_column(BOOLEAN, nullable=False, default=True)
    extend_existing = True

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id},"
                f"post={self.post},"
                f"description={self.description},"
                f"publication_date={self.publication_date},"
                f"level_skill={self.level_skill}"
                f"salary={self.salary},"
                f"id_employer={self.id_employer},"
                f"is_active={self.is_active})")

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "publication_date": self.publication_date,
            "level_skill": self.level_skill,
            "salary": self.salary,
            "id_employer": self.id_employer,
            "is_active": self.is_active,}


