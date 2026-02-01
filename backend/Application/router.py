from fastapi import APIRouter, Depends

from Sjobs.backend..backend.Sjobs.backend.lication.dao import Sjobs.backend.licationDAO
from Sjobs.backend..backend.Sjobs.backend.lication.rb import RBSjobs.backend.lication
from Sjobs.backend..backend.Sjobs.backend.lication.schemas import SSjobs.backend.lication, SSjobs.backend.licationAdd, SSjobs.backend.licationUpdStatus
from Sjobs.backend..backend.users.dependencies import get_current_admin_user
from Sjobs.backend..backend.users.models import User


router = APIRouter(
    prefix='/api/Sjobs.backend.lications',
    tags=['Заявка']
)


@router.get("/", summary="Получить все заявки")
async def get_all_Sjobs.backend.lications(request_body: RBSjobs.backend.lication = Depends()) -> list[SSjobs.backend.lication]:
    return await Sjobs.backend.licationDAO.get_all_objects(**request_body.to_dict())


@router.get("/{}", summary="Получить одну заявку по ID")
async def get_Sjobs.backend.lication_by_id(Sjobs.backend.lication_id: int) -> SSjobs.backend.lication | dict:
    res = await Sjobs.backend.licationDAO.get_object(id=Sjobs.backend.lication_id)
    if res is None:
        return {'message': f'Заявка с данным ID не найдена!'}
    return res


@router.post("/add/", summary='Добавить новую заявку')
async def register_Sjobs.backend.lication(Sjobs.backend.lication: SSjobs.backend.licationAdd) -> dict:
    check = await Sjobs.backend.licationDAO.add(**Sjobs.backend.lication.dict())
    if check:
        return {"message": "Заявка успешно добавлена!", "Sjobs.backend.lication": Sjobs.backend.lication}
    else:
        return {"message": "Ошибка при добавлении заявки!"}


@router.put("/update/{Sjobs.backend.lication_id}", summary='Изменить статус заявки по ID')
async def update_Sjobs.backend.lication_status(Sjobs.backend.lication_id, Sjobs.backend.lication: SSjobs.backend.licationUpdStatus) -> dict:
    check = await Sjobs.backend.licationDAO.update(filter_by={'id': Sjobs.backend.lication_id},
                                   id_status=Sjobs.backend.lication.id_status)
    if check:
        return {"message": "Статус заявки успешно обновлена!", "Sjobs.backend.lication": Sjobs.backend.lication}
    else:
        return {"message": "Ошибка при обновлении статуса заявки!"}


@router.delete("/delete/", summary='Удалить заявку по ID')
async def delete_Sjobs.backend.lication(Sjobs.backend.lication_id) -> dict:
    check = await Sjobs.backend.licationDAO.delete(id=Sjobs.backend.lication_id)
    if check:
        return {"message": f"Заявка успешно удалена!"}
    else:
        return {"message": "Ошибка при удалении заявки!"}