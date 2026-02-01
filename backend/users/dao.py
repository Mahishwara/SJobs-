from backend.dao.base import BaseDAO
from backend.users.models import User


class UsersDAO(BaseDAO):
    model = User
