from Sjobs.backend.dao.base import BaseDAO
from Sjobs.backend.Application.models import Application


class ApplicationDAO(BaseDAO):
    model = Application