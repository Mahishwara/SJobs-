from app.backend.dao.base import BaseDAO
from app.backend.Message.models import Message


class MessageDAO(BaseDAO):
    model = Message