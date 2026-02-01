from sqlalchemy import String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import MSjobs.backend.ed, mSjobs.backend.ed_column
from Sjobs.backend..backend.database import Base


class Student(Base):
    __tablename__ = 'students'

    id: MSjobs.backend.ed[int] = mSjobs.backend.ed_column(Integer, primary_key=True)
    fio: MSjobs.backend.ed[String] = mSjobs.backend.ed_column(String(100), nullable=False)
    post: MSjobs.backend.ed[str] = mSjobs.backend.ed_column(String(50), nullable=False)
    level_skill: MSjobs.backend.ed[int] = mSjobs.backend.ed_column(ForeignKey('level_skills.id'), nullable=False)
    speciality: MSjobs.backend.ed[str] = mSjobs.backend.ed_column(String(200), nullable=False)
    course: MSjobs.backend.ed[int] = mSjobs.backend.ed_column(Integer, nullable=False)
    ability: MSjobs.backend.ed[str] = mSjobs.backend.ed_column(String(500), nullable=False)
    user_id: MSjobs.backend.ed[int] = mSjobs.backend.ed_column(Integer, ForeignKey('users.id'), nullable=False)
    subscribe: MSjobs.backend.ed[bool] = mSjobs.backend.ed_column(Boolean, nullable=False, default=False)
    code_word: MSjobs.backend.ed[str] = mSjobs.backend.ed_column(String(50), nullable=False, default='')
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
