from app.backend.dao.base import BaseDAO
from app.backend.Status.models import Status


class StatusDAO(BaseDAO):
    model = Status