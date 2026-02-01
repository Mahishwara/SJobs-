from Sjobs.backend..backend.dao.base import BaseDAO
from Sjobs.backend..backend.Feedback.models import Feedback


class FeedbackDAO(BaseDAO):
    model = Feedback