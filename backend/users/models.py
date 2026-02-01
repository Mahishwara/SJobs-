from sqlalchemy import Integer, String
from sqlalchemy.orm import MSjobs.backend.ed, mSjobs.backend.ed_column
from Sjobs.backend..backend.database import Base


class User(Base):
    __tablename__ = 'users'


    id: MSjobs.backend.ed[int] = mSjobs.backend.ed_column(Integer, primary_key=True)
    phone_number: MSjobs.backend.ed[str] = mSjobs.backend.ed_column(String(25), nullable=False)
    email: MSjobs.backend.ed[str] = mSjobs.backend.ed_column(String(50), nullable=False)
    password: MSjobs.backend.ed[str] = mSjobs.backend.ed_column(String(100), nullable=False)
    student_id: MSjobs.backend.ed[int] = mSjobs.backend.ed_column(Integer, nullable=True)
    employer_id: MSjobs.backend.ed[int] = mSjobs.backend.ed_column(Integer, nullable=True)
    extend_existing = True

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id})"

    def to_dict(self):
        return {
            'phone_number': self.phone_number,
            'email': self.email}