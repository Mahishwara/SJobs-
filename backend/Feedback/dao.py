from app.backend.dao.base import BaseDAO
from app.backend.Feedback.models import Feedback


class FeedbackDAO(BaseDAO):
    model = Feedback