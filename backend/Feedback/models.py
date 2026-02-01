from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from Sjobs.backend.database import Base


class Feedback(Base):
    __tablename__ = 'feedbacks'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_to: Mapped[int] = mapped_column(Integer, nullable=False)
    id_from: Mapped[int] = mapped_column(Integer, nullable=False)
    rate: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(200), nullable=True)
    path: Mapped[int] = mapped_column(Integer, nullable=True)
    extend_existing = True

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id},"
                f"id_to={self.id_to!r}, "
                f"id_from={self.id_from!r}, "
                f"rate={self.rate!r}, "
                f"description={self.description!r},"
                f"path={self.path!r},)")

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            "id": self.id,
            "id_to": self.id_to,
            "id_from": self.id_from,
            "rate": self.rate,
            "description": self.description,
            "path": self.path}