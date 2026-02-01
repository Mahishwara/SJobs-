from backend.dao.base import BaseDAO
from backend.Interview.models import Interview


class InterviewDAO(BaseDAO):
    model = Interview


