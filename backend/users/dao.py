from Sjobs.backend.dao.base import BaseDAO
from Sjobs.backend.users.models import User


class UsersDAO(BaseDAO):
    model = User
