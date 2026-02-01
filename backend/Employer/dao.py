from backend.dao.base import BaseDAO
from backend.Employer.models import Employer


class EmployerDAO(BaseDAO):
    model = Employer