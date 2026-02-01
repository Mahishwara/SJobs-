from backend.dao.base import BaseDAO
from backend.Status.models import Status


class StatusDAO(BaseDAO):
    model = Status