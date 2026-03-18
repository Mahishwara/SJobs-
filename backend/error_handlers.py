"""
Модуль для обработки ошибок приложения
"""
from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError


async def validation_error_handler(request: Request, exc: RequestValidationError):
    """
    Обработчик ошибок валидации Pydantic.
    Форматирует ошибки в удобный для клиента формат.
    """
    errors = {}
    
    for error in exc.errors():
        field = '.'.join(str(loc) for loc in error['loc'][1:])
        
        # Если field пуст, значит ошибка на корне объекта
        if not field:
            field = 'body'
        
        error_msg = error['msg']
        
        if field not in errors:
            errors[field] = []
        
        errors[field].append(error_msg)
    
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "success": False,
            "message": "Ошибка валидации данных",
            "details": errors,
            "error_count": len(exc.errors())
        }
    )


class ValidationErrorResponse:
    """Класс для формирования стандартного ответа об ошибке валидации"""
    
    @staticmethod
    def error_response(message: str, errors: dict, status_code: int = 422):
        """Создать стандартный ответ об ошибке"""
        return {
            "success": False,
            "message": message,
            "details": errors,
            "error_count": len(errors)
        }
    
    @staticmethod
    def success_response(message: str = "Успешно", data: dict = None, status_code: int = 200):
        """Создать стандартный ответ об успехе"""
        response = {
            "success": True,
            "message": message,
        }
        if data:
            response["data"] = data
        return response
