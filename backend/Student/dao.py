from Sjobs.backend.dao.base import BaseDAO
from Sjobs.backend.Student.models import Student


class StudentDAO(BaseDAO):
    model = Student