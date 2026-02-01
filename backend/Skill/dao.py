from backend.dao.base import BaseDAO
from backend.Skill.models import Skill


class SkillDAO(BaseDAO):
    model = Skill