FROM python:3.11-slim-buster

# Рабочий каталог и установка зависимостей
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем проект
COPY . .

# Создаем стартовую миграцию (первоначальную структуру базы данных)
RUN alembic revision --autogenerate -m "initial migration"

# Применяем миграции (создаем структуру БД)
RUN alembic upgrade head

# Запускаем приложение
CMD ["uvicorn", "app.main:app", "--port", "8000"]