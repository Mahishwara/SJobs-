from Sjobs.backend..backend.dao.base import BaseDAO
from Sjobs.backend..backend.Status.models import Status


class StatusDAO(BaseDAO):
    model = Status