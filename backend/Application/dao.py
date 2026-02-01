from app.backend.dao.base import BaseDAO
from app.backend.Application.models import Application


class ApplicationDAO(BaseDAO):
    model = Application