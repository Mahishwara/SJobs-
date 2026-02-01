from Sjobs.backend.dao.base import BaseDAO
from Sjobs.backend.Status.models import Status


class StatusDAO(BaseDAO):
    model = Status