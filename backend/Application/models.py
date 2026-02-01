from sqlalchemy import String, Integer, ForeignKey, DATE, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from backend.database import Base
from datetime import date


class Application(Base):
    __tablename__ = 'applications'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_student: Mapped[int] = mapped_column(ForeignKey('students.id'), nullable=False)
    id_vacancy: Mapped[int] = mapped_column(ForeignKey('vacancies.id'), nullable=False)
    date: Mapped[date] = mapped_column(DATE, default=date.today())
    id_status: Mapped[int] = mapped_column(ForeignKey('statuses.id'), default=1)


    extend_existing = True

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id},"
                f"id_student={self.id_student},"
                f"id_vacancy={self.id_vacancy},"
                f"date={self.date},"
                f"status={self.status},")

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            "id": self.id,
            "id_student": self.id_student,
            "id_vacancy": self.id_vacancy,
            "date": self.date,
            "status": self.status}