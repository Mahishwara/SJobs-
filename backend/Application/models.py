from sqlalchemy import String, Integer, ForeignKey, DATE, Boolean
from sqlalchemy.orm import MSjobs.backend.ed, mSjobs.backend.ed_column
from Sjobs.backend..backend.database import Base
from datetime import date


class Sjobs.backend.lication(Base):
    __tablename__ = 'Sjobs.backend.lications'

    id: MSjobs.backend.ed[int] = mSjobs.backend.ed_column(Integer, primary_key=True)
    id_student: MSjobs.backend.ed[int] = mSjobs.backend.ed_column(ForeignKey('students.id'), nullable=False)
    id_vacancy: MSjobs.backend.ed[int] = mSjobs.backend.ed_column(ForeignKey('vacancies.id'), nullable=False)
    date: MSjobs.backend.ed[date] = mSjobs.backend.ed_column(DATE, default=date.today())
    id_status: MSjobs.backend.ed[int] = mSjobs.backend.ed_column(ForeignKey('statuses.id'), default=1)


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