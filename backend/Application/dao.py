from backend.dao.base import BaseDAO
from backend.Application.models import Application


class ApplicationDAO(BaseDAO):
    model = Application