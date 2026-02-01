from Sjobs.backend.dao.base import BaseDAO
from Sjobs.backend.Employer.models import Employer


class EmployerDAO(BaseDAO):
    model = Employer