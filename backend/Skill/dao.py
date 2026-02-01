from Sjobs.backend..backend.dao.base import BaseDAO
from Sjobs.backend..backend.Skill.models import Skill


class SkillDAO(BaseDAO):
    model = Skill