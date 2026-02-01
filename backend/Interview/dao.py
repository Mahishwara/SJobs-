from app.backend.dao.base import BaseDAO
from app.backend.Interview.models import Interview


class InterviewDAO(BaseDAO):
    model = Interview


