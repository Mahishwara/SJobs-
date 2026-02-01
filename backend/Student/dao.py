from app.backend.dao.base import BaseDAO
from app.backend.Student.models import Student


class StudentDAO(BaseDAO):
    model = Student