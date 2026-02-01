from fastapi import APIRouter, Depends

from Sjobs.backend.Message.dao import MessageDAO
from Sjobs.backend.Message.rb import RBMessage
from Sjobs.backend.Message.schemas import SMessage, SMessageAdd
from Sjobs.backend.users.dependencies import get_current_admin_user
from Sjobs.backend.users.models import User


router = APIRouter(
    prefix='/api/messages',
    tags=['Сообщения']
)


@router.get("/", summary="Получить все сообщения")
async def get_all_messages(request_body: RBMessage = Depends()) -> list[SMessage]:
    return await MessageDAO.get_all_objects(**request_body.to_dict())


@router.get("/{message_id}", summary="Получить одно сообщение по ID")
async def get_message_by_id(message_id: int) -> SMessage | dict:
    res = await MessageDAO.get_object(id=message_id)
    if res is None:
        return {'message': f'Сообщение с данным ID не найдена!'}
    return res


@router.get("/ordered/", summary="Получить все сообщения упорядоченные по новизне")
async def get_all_ordered_messages(request_body: RBMessage = Depends()) -> list[SMessage]:
    return await MessageDAO.get_all_objects_order_by('message', **request_body.to_dict())


@router.post("/add/", summary='Добавить новое сообщение')
async def register_message(message: SMessageAdd) -> dict:
    check = await MessageDAO.add(**message.dict())
    if check:
        return {"message": "Сообщение успешно добавлено!", "New message": message}
    else:
        return {"message": "Ошибка при добавлении сообщения!"}


@router.delete("/delete/{message_id}", summary='Удалить сообщение по ID')
async def delete_message(message_id) -> dict:
    check = await MessageDAO.delete(id=message_id)
    if check:
        return {"message": f"сообщение успешно удалено!"}
    else:
        return {"message": "Ошибка при удалении сообщения!"}