from sqlalchemy import String, Integer,DATE, ForeignKey, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.database import Base
import datetime


class Interview(Base):
    __tablename__ = 'interview'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_student: Mapped[int] = mapped_column(ForeignKey("students.id"), nullable=False)
    id_vacancy: Mapped[int] = mapped_column(ForeignKey("vacancies.id"), nullable=False)
    date_start: Mapped[datetime.date] = mapped_column(DATE, nullable=False)
    time_start: Mapped[datetime.time] = mapped_column(Time, nullable=False)

    extend_existing = True

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id},"
                f"id_student={self.id_student!r}, "
                f"id_vacancy={self.id_vacancy!r}, "
                f"date_start={self.date!r}),"
                f"time_start={self.time!r}")

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            "id": self.id,
            "id_student": self.id_student,
            "id_vacancy": self.id_vacancy,
            "date_start": self.date,
            "time_start": self.time,}