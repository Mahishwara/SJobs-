from Sjobs.backend..backend.dao.base import BaseDAO
from Sjobs.backend..backend.Employer.models import Employer


class EmployerDAO(BaseDAO):
    model = Employer