from fastapi import APIRouter, Depends

from app.backend.Employer.dao import EmployerDAO
from app.backend.Employer.rb import RBEmployer
from app.backend.Employer.schemas import SEmployer, SEmployerAdd, SEmployerUpd
from app.backend.users.dependencies import get_current_user
from app.backend.users.models import User
from app.backend.users.router import update_user


router = APIRouter(
    prefix='/api/employers',
    tags=['Работодатель']
)


@router.get("/", summary="Получить всех работодателей")
async def get_all_employers(request_body: RBEmployer = Depends()) -> list[SEmployer]:
    return await EmployerDAO.get_all_objects(**request_body.to_dict())


@router.get("/{employer_id}", summary="Получить одного работодателя по ID")
async def get_employer_by_id(employer_id: int) -> SEmployer | dict:
    res = await EmployerDAO.get_object(id=employer_id)
    if res is None:
        return {'message': f'Работодатель с данным ID не найдена!'}
    return res


@router.post("/add/", summary='Добавить нового работодателя')
async def register_employer(employer: SEmployerAdd, user_data: User = Depends(get_current_user)) -> dict:
    check = await EmployerDAO.add(**employer.dict())
    if check:
        await update_user(new_data={'student_id': None,
                                    'employer_id': check}, user_id=user_data.id)
        return {"message": "Работодатель успешно добавлен!", "employer": employer}
    else:
        return {"message": "Ошибка при добавлении работодателя!"}


@router.put("/update/{employer_id}", summary='Изменить работодателя по ID')
async def update_employer(employer_id, employer: SEmployerUpd) -> dict:
    check = await EmployerDAO.update(filter_by={'id': employer_id},
                                   name=employer.name, organization=employer.organization,
                                     description=employer.description)
    if check:
        return {"message": "Работодатель успешно обновлен!", "employer": employer}
    else:
        return {"message": "Ошибка при обновлении работодателя!"}


@router.delete("/delete/{employer_id}", summary='Удалить навык по ID')
async def delete_employer(employer_id) -> dict:
    check = await EmployerDAO.delete(id=employer_id)
    if check:
        return {"message": f"Работодатель успешно удален!"}
    else:
        return {"message": "Ошибка при удалении работодателя!"}