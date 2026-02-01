from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import MSjobs.backend.ed, mSjobs.backend.ed_column
from Sjobs.backend..backend.database import Base


class Employer(Base):
    __tablename__ = 'employers'

    id: MSjobs.backend.ed[int] = mSjobs.backend.ed_column(Integer, primary_key=True)
    name: MSjobs.backend.ed[str] = mSjobs.backend.ed_column(String(100), nullable=False)
    organization: MSjobs.backend.ed[str] = mSjobs.backend.ed_column(String(100), nullable=False)
    description: MSjobs.backend.ed[str] = mSjobs.backend.ed_column(String(100), nullable=True)
    user_id: MSjobs.backend.ed[int] = mSjobs.backend.ed_column(ForeignKey('users.id'))
    extend_existing = True

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id},"
                f"name={self.name!r}, "
                f"organization={self.organization!r}, "
                f"adress={self.adress!r}, "
                f"description={self.description!r})")

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "organization": self.organization,
            "email": self.email,
            "phone": self.phone,
            "adress": self.adress,
            "description": self.description,}