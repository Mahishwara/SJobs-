from fastapi import APIRouter, Depends

from backend.Application.dao import ApplicationDAO
from backend.Application.rb import RBApplication
from backend.Application.schemas import SApplication, SApplicationAdd, SApplicationUpdStatus
from backend.users.dependencies import get_current_admin_user
from backend.users.models import User


router = APIRouter(
    prefix='/api/applications',
    tags=['Заявка']
)


@router.get("/", summary="Получить все заявки")
async def get_all_applications(request_body: RBApplication = Depends()) -> list[SApplication]:
    return await ApplicationDAO.get_all_objects(**request_body.to_dict())


@router.get("/{}", summary="Получить одну заявку по ID")
async def get_application_by_id(application_id: int) -> SApplication | dict:
    res = await ApplicationDAO.get_object(id=application_id)
    if res is None:
        return {'message': f'Заявка с данным ID не найдена!'}
    return res


@router.post("/add/", summary='Добавить новую заявку')
async def register_application(application: SApplicationAdd) -> dict:
    check = await ApplicationDAO.add(**application.dict())
    if check:
        return {"message": "Заявка успешно добавлена!", "application": application}
    else:
        return {"message": "Ошибка при добавлении заявки!"}


@router.put("/update/{application_id}", summary='Изменить статус заявки по ID')
async def update_application_status(application_id, application: SApplicationUpdStatus) -> dict:
    check = await ApplicationDAO.update(filter_by={'id': application_id},
                                   id_status=application.id_status)
    if check:
        return {"message": "Статус заявки успешно обновлена!", "application": application}
    else:
        return {"message": "Ошибка при обновлении статуса заявки!"}


@router.delete("/delete/", summary='Удалить заявку по ID')
async def delete_application(application_id) -> dict:
    check = await ApplicationDAO.delete(id=application_id)
    if check:
        return {"message": f"Заявка успешно удалена!"}
    else:
        return {"message": "Ошибка при удалении заявки!"}