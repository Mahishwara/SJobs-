from fastapi import Request, HTTPException, status, Depends
import jwt
from jwt import PyJWTError
from datetime import datetime, timezone
from app.backend.config import get_auth_data
from app.backend.exceptions import TokenExpiredException, NoJwtException, NoUserIdException, ForbiddenException, TokenNoFound
from app.backend.users.dao import UsersDAO
from app.backend.users.models import User


def get_token(request: Request):
    token = request.cookies.get('users_access_token')
    if not token:
        raise TokenNoFound
    return token


async def get_current_user(token):
    try:
        auth_data = get_auth_data()
        payload = jwt.decode(token, auth_data['secret_key'], algorithms=auth_data['algorithm'])
    except PyJWTError:
        raise NoJwtException

    expire: str = payload.get('exp')
    expire_time = datetime.fromtimestamp(int(expire), tz=timezone.utc)
    if (not expire) or (expire_time < datetime.now(timezone.utc)):
        raise TokenExpiredException

    user_id: str = payload.get('sub')
    print(user_id)
    if not user_id:
        raise NoUserIdException

    user = await UsersDAO.get_object(id=int(user_id))
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='User not found')
    print(user)
    return user


async def get_current_admin_user(current_user: User = Depends()):
    if current_user.is_admin:
        return current_user
    raise ForbiddenException
