from fastapi import APIRouter, Depends

from app.backend.Feedback.dao import FeedbackDAO
from app.backend.Feedback.rb import RBFeedback
from app.backend.Feedback.schemas import SFeedback, SFeedbackAdd, SFeedbackUpd
from app.backend.users.dependencies import get_current_admin_user
from app.backend.users.models import User


router = APIRouter(
    prefix='/api/feedbacks',
    tags=['Отзыв']
)


@router.get("/", summary="Получить все отзывы")
async def get_all_feedbacks(request_body: RBFeedback = Depends()) -> list[SFeedback]:
    return await FeedbackDAO.get_all_objects(**request_body.to_dict())


@router.get("/{feedback_id}", summary="Получить один отзыв по ID")
async def get_feedback_by_id(feedback_id: int) -> SFeedback | dict:
    res = await FeedbackDAO.get_object(id=feedback_id)
    if res is None:
        return {'message': f'Отзыв с данным ID не найдена!'}
    return res


@router.post("/add/", summary='Добавить новый отзыв')
async def register_feedback(feedback: SFeedbackAdd) -> dict:
    check = await FeedbackDAO.add(**feedback.dict())
    if check:
        return {"message": "Отзыв успешно добавлен!", "New feedback": feedback}
    else:
        return {"message": "Ошибка при добавлении отзыва!"}


@router.put("/update/{feedback_id}", summary='Изменить отзыв по ID')
async def update_feedback(feedback_id, feedback: SFeedbackUpd) -> dict:
    check = await FeedbackDAO.update(filter_by={'id': feedback_id},
                                   description=feedback.description,
                                     rate=feedback.rate)
    if check:
        return {"message": "Отзыв успешно обновлен!", "feedback": feedback}
    else:
        return {"message": "Ошибка при обновлении отзыва!"}


@router.delete("/delete/{feedback_id}", summary='Удалить отзыв по ID')
async def delete_feedback(feedback_id) -> dict:
    check = await FeedbackDAO.delete(id=feedback_id)
    if check:
        return {"message": f"Отзыв успешно удален!"}
    else:
        return {"message": "Ошибка при удалении отзыва!"}