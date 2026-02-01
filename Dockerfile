FROM python:3.11-slim-buster

# Рабочий каталог и установка зависимостей
WORKDIR /Sjobs.backend.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем проект
COPY . .

# Применяем миграции (создаем структуру БД)
RUN alembic upgrade head

# Запускаем приложение
CMD ["uvicorn", "Sjobs.backend..main:Sjobs.backend.", "--port", "8000"]