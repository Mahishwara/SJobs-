from Sjobs.backend.dao.base import BaseDAO
from Sjobs.backend.Feedback.models import Feedback


class FeedbackDAO(BaseDAO):
    model = Feedback