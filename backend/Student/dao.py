from backend.dao.base import BaseDAO
from backend.Student.models import Student


class StudentDAO(BaseDAO):
    model = Student