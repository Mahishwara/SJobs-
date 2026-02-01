from scripts.regsetup import description
import datetime
from sqlalchemy import select, or_
from Sjobs.backend..backend.dao.base import BaseDAO
from Sjobs.backend..backend.Vacancy.models import Vacancy
from Sjobs.backend..backend.database import async_session_maker


class VacancyDAO(BaseDAO):
    model = Vacancy

    @classmethod
    async def get_recommended_objects(cls, code_word):
        """Возвращает все объекты модели."""
        async with async_session_maker() as session:
            query = (select(cls.model).filter(or_(cls.model.post.ilike(f'%{code_word}%'), cls.model.description.ilike(f'%{code_word}%')))
                     .where(cls.model.publication_date > (datetime.datetime.now() - datetime.timedelta(days=1)), cls.model.is_active == True))
            result = await session.execute(query)
            return result.scalars().all()