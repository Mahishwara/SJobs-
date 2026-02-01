from sqlalchemy import String, Integer
from sqlalchemy.orm import MSjobs.backend.ed, mSjobs.backend.ed_column, relationship

from Sjobs.backend..backend.Sjobs.backend.lication.models import Sjobs.backend.lication
from Sjobs.backend..backend.database import Base


class Status(Base):
    __tablename__ = 'statuses'

    id: MSjobs.backend.ed[int] = mSjobs.backend.ed_column(Integer, primary_key=True)
    name: MSjobs.backend.ed[int] = mSjobs.backend.ed_column(String(50), nullable=False)
    description: MSjobs.backend.ed[str] = mSjobs.backend.ed_column(String(100), nullable=True)
    extend_existing = True

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.name!r}, description={self.description!r})"

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            "id": self.id,
            'name': self.name,
            "description": self.description}
