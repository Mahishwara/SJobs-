from fastapi import APIRouter, Depends

from backend.Interview.dao import InterviewDAO
from backend.Interview.rb import RBInterview
from backend.Interview.schemas import SInterview, SInterviewAdd, SInterviewUpd
from backend.users.dependencies import get_current_admin_user
from backend.users.models import User


router = APIRouter(
    prefix='/api/interviews',
    tags=['Собеседования']
)


@router.get("/", summary="Получить все собеседования")
async def get_all_interviews(request_body: RBInterview = Depends()) -> list[SInterview]:
    return await InterviewDAO.get_all_objects(**request_body.to_dict())


@router.get("/ordered", summary="Получить все собеседования")
async def get_all_ordered_interviews(request_body: RBInterview = Depends()) -> list[SInterview]:
    return await InterviewDAO.get_all_objects_order_by('interview', **request_body.to_dict())


@router.get("/{}", summary="Получить одно собеседование по ID")
async def get_interview_by_id(interview_id: int) -> SInterview | dict:
    res = await InterviewDAO.get_object(id=interview_id)
    if res is None:
        return {'message': f'Собеседование с данным ID не найдена!'}
    return res


@router.post("/add/", summary='Добавить новое собеседование')
async def register_interview(interview: SInterviewAdd) -> dict:
    check = await InterviewDAO.add(**interview.dict())
    if check:
        return {"message": "Собеседование успешно добавлено!", "New interview": interview}
    else:
        return {"message": "Ошибка при добавлении себеседования!"}


@router.put("/update/{interview_id}", summary='Изменить дату собеседования по ID')
async def update_interview(interview_id, interview: SInterviewUpd) -> dict:
    check = await InterviewDAO.update(filter_by={'id': interview_id},
                                   date_start=interview.date_start,
                                      time_start=interview.time_start)
    if check:
        return {"message": "Дата собеседования успешно обновлена!", "interview": interview}
    else:
        return {"message": "Ошибка при обновлении даты собеседования!"}


@router.delete("/delete/{interview_id}", summary='Удалить собеседование по ID')
async def delete_interview(interview_id) -> dict:
    check = await InterviewDAO.delete(id=interview_id)
    if check:
        return {"message": f"Собеседование успешно удалено!"}
    else:
        return {"message": "Ошибка при удалении собеседования!"}