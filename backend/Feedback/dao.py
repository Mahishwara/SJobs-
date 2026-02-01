from backend.dao.base import BaseDAO
from backend.Feedback.models import Feedback


class FeedbackDAO(BaseDAO):
    model = Feedback