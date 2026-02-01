from app.backend.dao.base import BaseDAO
from app.backend.Employer.models import Employer


class EmployerDAO(BaseDAO):
    model = Employer