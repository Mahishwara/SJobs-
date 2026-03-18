"""
Модуль для валидации данных
Содержит правила валидации для всех типов данных в приложении
"""
from datetime import datetime, date
from typing import Optional
import re


class ValidationRules:
    """Набор правил валидации для различных типов данных"""
    
    # ФИО
    FIO_MIN_LENGTH = 3
    FIO_MAX_LENGTH = 100
    FIO_PATTERN = r'^[а-яёА-ЯЁa-zA-Z\s\-]+$'
    
    # Email
    EMAIL_PATTERN = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Телефон
    PHONE_PATTERN = r'^\+?[1-9]\d{1,14}$'
    
    # Пароль
    PASSWORD_MIN_LENGTH = 8
    PASSWORD_MAX_LENGTH = 128
    
    # Текстовые поля
    DESCRIPTION_MIN_LENGTH = 3
    DESCRIPTION_MAX_LENGTH = 500
    
    SHORT_STRING_MIN = 1
    SHORT_STRING_MAX = 100
    
    # Числовые поля
    SALARY_MIN = 0
    SALARY_MAX = 1000000
    
    COURSE_MIN = 1
    COURSE_MAX = 6
    
    # Даты
    DATE_FORMAT = '%Y-%m-%d'


class FieldValidator:
    """Класс для валидации отдельных полей"""
    
    @staticmethod
    def validate_fio(value: str) -> str:
        """Валидация ФИО"""
        if not value:
            raise ValueError('ФИО обязательно')
        
        if len(value) < ValidationRules.FIO_MIN_LENGTH:
            raise ValueError(f'ФИО должно содержать минимум {ValidationRules.FIO_MIN_LENGTH} символов')
        
        if len(value) > ValidationRules.FIO_MAX_LENGTH:
            raise ValueError(f'ФИО не должно содержать более {ValidationRules.FIO_MAX_LENGTH} символов')
        
        if not re.match(ValidationRules.FIO_PATTERN, value):
            raise ValueError('ФИО должно содержать только буквы, пробелы и дефисы')
        
        return value.strip()
    
    @staticmethod
    def validate_email(value: str) -> str:
        """Валидация email"""
        if not value:
            raise ValueError('Email обязателен')
        
        if not re.match(ValidationRules.EMAIL_PATTERN, value):
            raise ValueError('Некорректный формат email')
        
        if len(value) > 255:
            raise ValueError('Email не должен превышать 255 символов')
        
        return value.lower().strip()
    
    @staticmethod
    def validate_phone(value: str) -> str:
        """Валидация телефона"""
        if not value:
            raise ValueError('Телефон обязателен')
        
        # Удаляем все символы кроме цифр и плюса
        cleaned = re.sub(r'[^\d+]', '', value)
        
        if not re.match(ValidationRules.PHONE_PATTERN, cleaned):
            raise ValueError('Некорректный формат телефона. Ожидается формат: +7XXXXXXXXXX или 89XXXXXXXXX')
        
        return cleaned
    
    @staticmethod
    def validate_password(value: str) -> str:
        """Валидация пароля"""
        if not value:
            raise ValueError('Пароль обязателен')
        
        if len(value) < ValidationRules.PASSWORD_MIN_LENGTH:
            raise ValueError(f'Пароль должен содержать минимум {ValidationRules.PASSWORD_MIN_LENGTH} символов')
        
        if len(value) > ValidationRules.PASSWORD_MAX_LENGTH:
            raise ValueError(f'Пароль не должен превышать {ValidationRules.PASSWORD_MAX_LENGTH} символов')
        
        # Проверка на наличие букв и цифр
        if not re.search(r'[a-zA-Z]', value) or not re.search(r'\d', value):
            raise ValueError('Пароль должен содержать буквы и цифры')
        
        return value
    
    @staticmethod
    def validate_string(value: str, min_length: int = 1, max_length: int = 100, 
                       field_name: str = 'Поле') -> str:
        """Валидация строкового поля"""
        if not value:
            raise ValueError(f'{field_name} обязательно')
        
        if len(value) < min_length:
            raise ValueError(f'{field_name} должно содержать минимум {min_length} символов')
        
        if len(value) > max_length:
            raise ValueError(f'{field_name} не должно содержать более {max_length} символов')
        
        return value.strip()
    
    @staticmethod
    def validate_salary(value: int) -> int:
        """Валидация зарплаты"""
        if not isinstance(value, int):
            raise ValueError('Зарплата должна быть числом')
        
        if value < ValidationRules.SALARY_MIN:
            raise ValueError(f'Зарплата не может быть меньше {ValidationRules.SALARY_MIN}')
        
        if value > ValidationRules.SALARY_MAX:
            raise ValueError(f'Зарплата не должна превышать {ValidationRules.SALARY_MAX}')
        
        return value
    
    @staticmethod
    def validate_course(value: int) -> int:
        """Валидация номера курса"""
        if not isinstance(value, int):
            raise ValueError('Номер курса должен быть числом')
        
        if value < ValidationRules.COURSE_MIN or value > ValidationRules.COURSE_MAX:
            raise ValueError(f'Номер курса должен быть от {ValidationRules.COURSE_MIN} до {ValidationRules.COURSE_MAX}')
        
        return value
    
    @staticmethod
    def validate_date(value: str, field_name: str = 'Дата', future_required: bool = True) -> date:
        """Валидация даты"""
        if not value:
            raise ValueError(f'{field_name} обязательна')
        
        try:
            parsed_date = datetime.strptime(value, ValidationRules.DATE_FORMAT).date()
        except ValueError:
            raise ValueError(f'{field_name} должна быть в формате ГГГГ-ММ-ДД')
        
        if future_required and parsed_date <= date.today():
            raise ValueError(f'{field_name} должна быть позже сегодняшнего дня')
        
        return parsed_date
    
    @staticmethod
    def validate_date_range(date_begin: date, date_end: date) -> tuple:
        """Валидация диапазона дат"""
        if date_begin >= date_end:
            raise ValueError('Дата начала должна быть раньше даты окончания')
        
        return date_begin, date_end
    
    @staticmethod
    def validate_positive_int(value: int, field_name: str = 'Значение') -> int:
        """Валидация положительного целого числа"""
        if not isinstance(value, int):
            raise ValueError(f'{field_name} должно быть числом')
        
        if value <= 0:
            raise ValueError(f'{field_name} должно быть положительным числом')
        
        return value


class ValidationErrors:
    """Класс для сбора и форматирования ошибок валидации"""
    
    def __init__(self):
        self.errors = {}
    
    def add_error(self, field: str, message: str):
        """Добавить ошибку для поля"""
        if field not in self.errors:
            self.errors[field] = []
        self.errors[field].append(message)
    
    def has_errors(self) -> bool:
        """Проверить наличие ошибок"""
        return len(self.errors) > 0
    
    def get_errors(self) -> dict:
        """Получить словарь ошибок"""
        return self.errors
    
    def format_message(self) -> str:
        """Форматировать ошибки в сообщение"""
        if not self.has_errors():
            return ''
        
        message_parts = []
        for field, messages in self.errors.items():
            for msg in messages:
                message_parts.append(f'{field}: {msg}')
        
        return '; '.join(message_parts)
