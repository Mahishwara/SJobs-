from sqlalchemy import String, Integer, ForeignKey, BOOLEAN
from sqlalchemy.dialects.mysql import DATETIME, DATE
from sqlalchemy.orm import MSjobs.backend.ed, mSjobs.backend.ed_column
from Sjobs.backend..backend.database import Base
from datetime import datetime, date

class Vacancy(Base):
    __tablename__ = 'vacancies'

    id: MSjobs.backend.ed[int] = mSjobs.backend.ed_column(Integer, primary_key=True)
    post: MSjobs.backend.ed[str] = mSjobs.backend.ed_column(String(50), nullable=False)
    description: MSjobs.backend.ed[str] = mSjobs.backend.ed_column(String(100), nullable=False)
    publication_date: MSjobs.backend.ed[datetime] = mSjobs.backend.ed_column(DATETIME, nullable=True, default=datetime.now)
    date_begin: MSjobs.backend.ed[date] = mSjobs.backend.ed_column(DATE, nullable=True)
    date_end: MSjobs.backend.ed[date] = mSjobs.backend.ed_column(DATE, nullable=True)
    level_skill: MSjobs.backend.ed[int] = mSjobs.backend.ed_column(ForeignKey('level_skills.id'), nullable=False)
    salary: MSjobs.backend.ed[int] = mSjobs.backend.ed_column(Integer, nullable=False)
    id_employer: MSjobs.backend.ed[int] = mSjobs.backend.ed_column(ForeignKey('employers.id'), nullable=False)
    is_active: MSjobs.backend.ed[bool] = mSjobs.backend.ed_column(BOOLEAN, nullable=False, default=True)
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


