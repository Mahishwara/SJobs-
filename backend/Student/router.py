from fastapi import APIRouter, Depends

from Sjobs.backend..backend.Student.dao import StudentDAO
from Sjobs.backend..backend.Student.rb import RBStudent
from Sjobs.backend..backend.Student.schemas import SStudent, SStudentAdd, SStudentUpd
from Sjobs.backend..backend.users.router import update_user
from Sjobs.backend..backend.users.dependencies import get_current_user
from Sjobs.backend..backend.users.models import User
from Sjobs.backend..backend.users.router import update_user

router = APIRouter(
    prefix='/api/students',
    tags=['Студент']
)


@router.get("/", summary="Получить всех студентов")
async def get_all_students(request_body: RBStudent = Depends()) -> list[SStudent]:
    return await StudentDAO.get_all_objects(**request_body.to_dict())


@router.get("/{student_id}", summary="Получить одного студента по ID")
async def get_student_by_id(student_id: int) -> SStudent | dict:
    res = await StudentDAO.get_object(id=student_id)
    if res is None:
        return {'message': f'Студент с данным ID не найдена!'}
    return res


@router.post("/add/", summary='Добавить нового студента')
async def register_student(student: SStudentAdd, user_data: User = Depends(get_current_user)) -> dict:
    student = student.dict()
    student['user_id'] = user_data.id
    check = await StudentDAO.add(**student)
    if check:
        await update_user(new_data={'student_id': check,
                              'employer_id': None}, user_id=user_data.id)
        return {"message": "Студент успешно добавлена!", "student": student}

    else:
        return {"message": "Ошибка при добавлении категории!"}


@router.put("/update/{student_id}", summary='Изменить студента')
async def update_student(student_id, student: SStudentUpd) -> dict:
    check = await StudentDAO.update(filter_by={'id': student_id},
                                    fio=student.fio,
                                    post=student.post,
                                    level_skill=student.level_skill,
                                    speciality=student.speciality,
                                    course=student.course,
                                    ability=student.ability,
                                    subscribe=student.subscribe,
                                    code_word=student.code_word)
    if check:
        return {"message": f"Данные студента успешно обновлены", "student": student}
    else:
        return {"message": "Ошибка при обновлении данных студента!"}


@router.delete("/delete/{student_id}", summary='Удалить студента по ID')
async def delete_student(request_body: RBStudent = Depends()) -> dict:
    check = await StudentDAO.delete(**request_body.to_dict())
    if check:
        return {"message": f"Студент успешно удален!"}
    else:
        return {"message": "Ошибка при удалении студента!"}