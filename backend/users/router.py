from fastapi import APIRouter, Response, Depends
from backend.exceptions import UserAlreadyExistsException, IncorrectEmailOrPasswordException
from backend.users.auth import get_password_hash, authenticate_user, create_access_token
from backend.users.dao import UsersDAO
from backend.users.dependencies import  get_current_admin_user, get_current_user
from backend.users.models import User
from backend.users.schemas import SUserRegister, SUserAuth, SUser, SToken
from backend.users.rb import RBUser, RBToken
from fastapi import Request

router = APIRouter(prefix='/api/auth', tags=['Пользователь'])


@router.post("/register/")
async def register_user(user_data: SUserRegister) -> dict:
    user = await UsersDAO.get_object(email=user_data.email)
    if user:
        raise UserAlreadyExistsException
    user_dict = user_data.dict()
    user_dict['password'] = get_password_hash(user_data.password)
    await UsersDAO.add(**user_dict)
    return {'message': f'Вы успешно зарегистрированы!'}


@router.post("/login/")
async def auth_user(response: Response, user_data: SUserAuth):
    check = await authenticate_user(email=user_data.email, password=user_data.password)
    if check is None:
        raise IncorrectEmailOrPasswordException
    access_token = create_access_token({"sub": str(check.id)})
    response.set_cookie(key="users_access_token", value=access_token, httponly=True)
    return {'ok': True, 'access_token': access_token, 'refresh_token': None, 'message': 'Авторизация успешна!'}


@router.post("/logout/")
async def logout_user(response: Response):
    response.delete_cookie(key="users_access_token")
    return {'message': 'Пользователь успешно вышел из системы'}


@router.get("/me/")
async def get_me(request_body: RBToken = Depends()):
    print(request_body)
    request_body = request_body.to_dict()
    print(request_body)
    user_data = await get_current_user(request_body['token'])
    return user_data


@router.get("/all_users/")
async def get_all_users(request_body: RBUser = Depends()):
    return await UsersDAO.get_all_objects(**request_body.to_dict())


@router.get("/")
async def get_users(request_body: RBUser = Depends()) -> list[SUser]:
    return await UsersDAO.get_all_objects(**request_body.to_dict())

@router.get("/me/update")
async def update_user(new_data, user_id):
    if new_data['student_id'] is not None:
        check = await UsersDAO.update(filter_by={'id': user_id},
                                        student_id=new_data['student_id'])
    if new_data['employer_id'] is not None:
        check = await UsersDAO.update(filter_by={'id': user_id},
                                        employer_id=new_data['employer_id'])
