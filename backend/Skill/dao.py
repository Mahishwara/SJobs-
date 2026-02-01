from app.backend.dao.base import BaseDAO
from app.backend.Skill.models import Skill


class SkillDAO(BaseDAO):
    model = Skill