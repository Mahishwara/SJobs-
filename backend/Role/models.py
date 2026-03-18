from sqlalchemy import String, Integer, ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column
from backend.database import Base


class Role(Base):
    __tablename__ = 'roles'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    role_name: Mapped[str] = mapped_column(String(50), nullable=False)
    role_type: Mapped[str] = mapped_column(String(50), nullable=False)  # 'student' or 'employer'
    description: Mapped[str] = mapped_column(String(500), nullable=True)
    permissions: Mapped[list] = mapped_column(JSON, nullable=False, default=list)
    
    extend_existing = True

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id},"
                f"role_name={self.role_name!r}, "
                f"role_type={self.role_type!r})")

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            "id": self.id,
            "role_name": self.role_name,
            "role_type": self.role_type,
            "description": self.description,
            "permissions": self.permissions,
        }
