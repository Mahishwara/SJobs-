from backend.dao.base import BaseDAO
from backend.Role.models import Role


class RoleDAO(BaseDAO):
    model = Role
