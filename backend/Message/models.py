from sqlalchemy import String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from app.backend.database import Base
from datetime import datetime


class Message(Base):
    __tablename__ = 'messages'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_student: Mapped[int] = mapped_column(ForeignKey('students.id'), nullable=False)
    id_vacancy: Mapped[int] = mapped_column(ForeignKey('vacancies.id'), nullable=False)
    description: Mapped[str] = mapped_column(String(100), nullable=True)
    path_type: Mapped[int] = mapped_column(Integer, nullable=True)
    date_publicated: Mapped[datetime] = mapped_column(DateTime, nullable=True, default=datetime.now())
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