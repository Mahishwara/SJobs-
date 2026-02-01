from Sjobs.backend..backend.dao.base import BaseDAO
from Sjobs.backend..backend.users.models import User


class UsersDAO(BaseDAO):
    model = User
