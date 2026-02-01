from Sjobs.backend..backend.dao.base import BaseDAO
from Sjobs.backend..backend.Message.models import Message


class MessageDAO(BaseDAO):
    model = Message