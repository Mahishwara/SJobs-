from fastapi import APIRouter, Depends

from backend.Role.dao import RoleDAO
from backend.Role.rb import RBRole
from backend.Role.schemas import SRole, SRoleAdd, SRoleUpd
from backend.users.dependencies import get_current_admin_user
from backend.users.models import User


router = APIRouter(
    prefix='/api/roles',
    tags=['Роли']
)


@router.get("/", summary="Получить все роли")
async def get_all_roles(request_body: RBRole = Depends()) -> list[SRole]:
    return await RoleDAO.get_all_objects(**request_body.to_dict())


@router.get("/{role_id}", summary="Получить одну роль по ID")
async def get_role_by_id(role_id: int) -> SRole | dict:
    res = await RoleDAO.get_object(id=role_id)
    if res is None:
        return {'message': f'Роль с данным ID не найдена!'}
    return res


@router.post("/add/", summary='Добавить новую роль')
async def add_role(role: SRoleAdd) -> dict:
    check = await RoleDAO.add(**role.dict())
    if check:
        return {"message": "Роль успешно добавлена!", "New role": role}
    else:
        return {"message": "Ошибка при добавлении роли!"}


@router.put("/update/{role_id}", summary='Изменить роль по ID')
async def update_role(role_id: int, role: SRoleUpd) -> dict:
    update_data = {k: v for k, v in role.dict().items() if v is not None}
    check = await RoleDAO.update(filter_by={'id': role_id}, **update_data)
    if check:
        return {"message": "Роль успешно обновлена!", "role": role}
    else:
        return {"message": "Ошибка при обновлении роли!"}


@router.delete("/delete/{role_id}", summary='Удалить роль по ID')
async def delete_role(role_id: int) -> dict:
    check = await RoleDAO.delete(id=role_id)
    if check:
        return {"message": f"Роль успешно удалена!"}
    else:
        return {"message": "Ошибка при удалении роли!"}
