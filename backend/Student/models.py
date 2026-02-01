from sqlalchemy import String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from backend.database import Base


class Student(Base):
    __tablename__ = 'students'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fio: Mapped[String] = mapped_column(String(100), nullable=False)
    post: Mapped[str] = mapped_column(String(50), nullable=False)
    level_skill: Mapped[int] = mapped_column(ForeignKey('level_skills.id'), nullable=False)
    speciality: Mapped[str] = mapped_column(String(200), nullable=False)
    course: Mapped[int] = mapped_column(Integer, nullable=False)
    ability: Mapped[str] = mapped_column(String(500), nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'), nullable=False)
    subscribe: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    code_word: Mapped[str] = mapped_column(String(50), nullable=False, default='')
    extend_existing = True

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id})")

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            "id": self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'post': self.post,
            'level_skill': self.level_skill,
            'speciality': self.speciality,
            'course': self.course,
            'ability': self.ability,
            'subscribe': self.subscribe,
            'code_word': self.code_word}
