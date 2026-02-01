from Sjobs.backend.dao.base import BaseDAO
from Sjobs.backend.Interview.models import Interview


class InterviewDAO(BaseDAO):
    model = Interview


