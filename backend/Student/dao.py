from Sjobs.backend..backend.dao.base import BaseDAO
from Sjobs.backend..backend.Student.models import Student


class StudentDAO(BaseDAO):
    model = Student