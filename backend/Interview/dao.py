from Sjobs.backend..backend.dao.base import BaseDAO
from Sjobs.backend..backend.Interview.models import Interview


class InterviewDAO(BaseDAO):
    model = Interview


