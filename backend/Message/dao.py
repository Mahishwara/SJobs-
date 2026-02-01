from backend.dao.base import BaseDAO
from backend.Message.models import Message


class MessageDAO(BaseDAO):
    model = Message