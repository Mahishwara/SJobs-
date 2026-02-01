from fastapi import APIRouter, Depends
from app.backend.Vacancy.dao import VacancyDAO
from app.backend.Vacancy.rb import RBVacancy
from app.backend.Vacancy.schemas import SVacancy, SVacancyAdd, SVacancyUpd, SVacancyUpdActive
from app.backend.users.dependencies import get_current_admin_user
from app.backend.users.models import User


router = APIRouter(
    prefix='/api/vacancies',
    tags=['Вакансии']
)


@router.get("/", summary="Получить все вакансии")
async def get_all_vacancies(request_body: RBVacancy = Depends()) -> list[SVacancy]:
    return await VacancyDAO.get_all_objects(**request_body.to_dict())


@router.get("/recommended/", summary="Получить все вакансии")
async def get_all_recommended_vacancies(code_word) -> list[SVacancy]:
    return await VacancyDAO.get_recommended_objects(code_word)


@router.get("/find/", summary="Получить все вакансии")
async def find_vacancies(field, text) -> list[SVacancy]:
    return await VacancyDAO.find_objects(field, text)

@router.get("/{vacancy_id}", summary="Получить одну вакансию по ID")
async def get_vacancy_by_id(vacancy_id: int) -> SVacancy | dict:
    res = await VacancyDAO.get_object(id=vacancy_id)
    if res is None:
        return {'message': f'Вакансия с данным ID не найдена!'}
    return res


@router.post("/add/", summary='Добавить новую вакансия')
async def register_vacancy(vacancy: SVacancyAdd) -> dict:
    check = await VacancyDAO.add(**vacancy.dict())
    if check:
        return {"message": "Вакансию успешно добавлена!", "vacancy": vacancy}
    else:
        return {"message": "Ошибка при добавлении вакансии!"}


@router.put("/update/{vacancy_id}", summary='Изменить вакансию по ID')
async def update_vacancy(vacancy_id, vacancy: SVacancyUpd) -> dict:
    check = await VacancyDAO.update(filter_by={'id': vacancy_id},
                                   post=vacancy.post, description=vacancy.description,
                                    level_skill=vacancy.level_skill,
                                    salary=vacancy.salary,
                                    date_begin=vacancy.date_begin,
                                    date_end=vacancy.date_end
                                    )
    if check:
        return {"message": "Вакансия успешно обновлена!", "vacancy": vacancy}
    else:
        return {"message": "Ошибка при обновлении вакансии!"}


@router.put("/updateActive/{vacancy_id}", summary='Изменить вакансию по ID')
async def update_vacancy_active(vacancy_id, vacancy: SVacancyUpdActive) -> dict:
    check = await VacancyDAO.update(filter_by={'id': vacancy_id},
                                    is_active=vacancy.is_active)
    if check:
        return {"ok": True, "message": "Активность вакансии успешно обновлена!", "vacancy": vacancy}
    else:
        return {"message": "Ошибка при обновлении активности вакансии!"}


@router.delete("/delete/{vacancy_id}", summary='Удалить вакансию по ID')
async def delete_vacancy(vacancy_id) -> dict:
    check = await VacancyDAO.delete(id=vacancy_id)
    if check:
        return {"message": f"Вакансия успешно удалена!"}
    else:
        return {"message": "Ошибка при удалении вакансии!"}