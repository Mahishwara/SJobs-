from fastapi import APIRouter, Depends

from Sjobs.backend..backend.Status.dao import StatusDAO
from Sjobs.backend..backend.Status.rb import RBStatus
from Sjobs.backend..backend.Status.schemas import SStatus, SStatusAdd, SStatusUpd
from Sjobs.backend..backend.users.dependencies import get_current_admin_user
from Sjobs.backend..backend.users.models import User

router = APIRouter(
    prefix='/api/statuses',
    tags=['Статус']
)


@router.get("/", summary="Получить все статусы")
async def get_all_statuses(request_body: RBStatus = Depends()) -> list[SStatus]:
    return await StatusDAO.get_all_objects(**request_body.to_dict())


@router.get("/{}", summary="Получить один статус по ID")
async def get_status_by_id(status_id: int) -> SStatus | dict:
    res = await StatusDAO.get_object(id=status_id)
    if res is None:
        return {'message': f'Статус с данным ID не найдена!'}
    return res


@router.post("/add/", summary='Добавить новый статус')
async def register_status(status: SStatusAdd) -> dict:
    check = await StatusDAO.add(**status.dict())
    if check:
        return {"message": "Статус успешно добавлен!", "Статус": status}
    else:
        return {"message": "Ошибка при добавлении статуса!"}


@router.put("/update/{status_id}", summary='Изменить статус')
async def update_status(status_id, status: SStatusUpd,) -> dict:
    check = await StatusDAO.update(filter_by={'id': status_id},
                                    name=status.name,
                                    description=status.description)
    if check:
        return {"message": f"Данные статуса успешно обновлены", "status": status}
    else:
        return {"message": "Ошибка при обновлении данных статуса!"}


@router.delete("/delete/{status_id}", summary='Удалить статус по ID')
async def delete_status(request_body: RBStatus = Depends()) -> dict:
    check = await StatusDAO.delete(**request_body.to_dict())
    if check:
        return {"message": f"Статус успешно удален!"}
    else:
        return {"message": "Ошибка при удалении статуса!"}