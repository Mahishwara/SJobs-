from sqlalchemy import String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import MSjobs.backend.ed, mSjobs.backend.ed_column
from Sjobs.backend..backend.database import Base
from datetime import datetime


class Message(Base):
    __tablename__ = 'messages'

    id: MSjobs.backend.ed[int] = mSjobs.backend.ed_column(Integer, primary_key=True)
    id_student: MSjobs.backend.ed[int] = mSjobs.backend.ed_column(ForeignKey('students.id'), nullable=False)
    id_vacancy: MSjobs.backend.ed[int] = mSjobs.backend.ed_column(ForeignKey('vacancies.id'), nullable=False)
    description: MSjobs.backend.ed[str] = mSjobs.backend.ed_column(String(100), nullable=True)
    path_type: MSjobs.backend.ed[int] = mSjobs.backend.ed_column(Integer, nullable=True)
    date_publicated: MSjobs.backend.ed[datetime] = mSjobs.backend.ed_column(DateTime, nullable=True, default=datetime.now())
    extend_existing = True

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, id_student={self.id_student}, id_vacancy={self.id_vacancy}, path_type={self.path_type}, description={self.description!r})"

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            "id": self.id,
            "id_student": self.id_student,
            "id_vacancy": self.id_vacancy,
            "path_type": self.path_type,
            "description": self.description,}