from fastapi import APIRouter, Depends

from backend.Skill.dao import SkillDAO
from backend.Skill.rb import RBSkill
from backend.Skill.schemas import SSkill, SSkillAdd, SSkillUpd
from backend.users.dependencies import get_current_admin_user
from backend.users.models import User


router = APIRouter(
    prefix='/api/skills',
    tags=['Уровень навыков']
)


@router.get("/", summary="Получить все уровни навыков")
async def get_all_skills(request_body: RBSkill = Depends()) -> list[SSkill]:
    return await SkillDAO.get_all_objects(**request_body.to_dict())


@router.get("/{skill_id}", summary="Получить один уровень по ID")
async def get_skill_by_id(skill_id: int) -> SSkill | dict:
    res = await SkillDAO.get_object(id=skill_id)
    if res is None:
        return {'message': f'Уровень с данным ID не найдена!'}
    return res


@router.post("/add/", summary='Добавить новый навык')
async def register_skill(skill: SSkillAdd) -> dict:
    check = await SkillDAO.add(**skill.dict())
    if check:
        return {"message": "Уровень успешно добавлен!", "skill": skill}
    else:
        return {"message": "Ошибка при добавлении уровня!"}


@router.put("/update/{skill_id}", summary='Изменить уровень')
async def update_skill(skill_id, skill: SSkillUpd) -> dict:
    check = await SkillDAO.update(filter_by={'id': skill_id},
                                   level=skill.level)
    if check:
        return {"message": "Уровень успешно обновлен!", "skill": skill}
    else:
        return {"message": "Ошибка при обновлении уровеня!"}


@router.delete("/delete/{skill_id}", summary='Удалить уровень по ID')
async def delete_skill(skill_id) -> dict:
    check = await SkillDAO.delete(id=skill_id)
    if check:
        return {"message": f"Уровень успешно удален!"}
    else:
        return {"message": "Ошибка при удалении уровня!"}