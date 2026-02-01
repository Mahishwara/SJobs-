from Sjobs.backend.dao.base import BaseDAO
from Sjobs.backend.Message.models import Message


class MessageDAO(BaseDAO):
    model = Message