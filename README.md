# Online Grade Book

## Описание

Этот проект представляет собой электронный дневник для ученикников, позволяющий управлять данными о учениках и их оценками. Реализованы функции создания, чтения, обновления и удаления (CRUD) для учеников и их оценок.

## Требования

Для запуска проекта необходимы следующие компоненты:

- Python 3.8 или выше
- Виртуальное окружение (рекомендуется)
- SQLite (или другой поддерживаемый SQLAlchemy СУБД)

## Установка

### 1. Клонирование репозитория

Склонируйте репозиторий с GitHub:
git clone https://github.com/yerbolatik/online-grade-book.git
cd online-grade-book

### 2. Создание и активация виртуального окружения

Создайте виртуальное окружение:
python -m venv .venv

Активируйте виртуальное окружение:

- На Windows:
  .\.venv\Scripts\activate
- На macOS/Linux:
  source .venv/bin/activate

### 3. Установка зависимостей

Установите необходимые зависимости с помощью pip:
pip install -r requirements.txt

### 4. Запуск проекта

Запустите сервер FastAPI:
uvicorn api.main:app --reload

Теперь ваше приложение должно быть доступно по адресу http://127.0.0.1:8000.

## Использование

### Работа с API

Приложение предоставляет следующие основные эндпоинты:

1. Создание ученика: POST /students/
2. Получение информации о ученике: GET /students/{student_id}
3. Обновление данных ученика: PATCH /students/{student_id}
4. Удаление ученика: DELETE /students/{student_id}
5. Создание оценки: POST /scores/
6. Получение информации об оценке: GET /scores/{score_id}
7. Обновление оценки: PATCH /scores/{score_id}
8. Удаление оценки: DELETE /scores/{score_id}

Пример запроса для создания ученика:
POST/students/
{
"first_name": "Yerbolat",
"last_name": "Assabay",
"age": 12,
"grade": 5
}

Пример запроса для создания оценки:
POST/scores/
{
"subject": "Math",
"score": 5,
"student_id": 1
}

Пример получения информации о конкретном ученике.
GET/students/1/
{
"first_name": "Yerbolat",
"last_name": "Assabay",
"age": 12,
"grade": 5,
"id": 1,
"scores": [
{
"subject": "Math",
"score": 5,
"id": 1,
"student_id": 1,
"created": "28 May 2024 20:33:46"
}
]
}

Пример получения информации о конкретной оценке.
{
"subject": "Math",
"score": 5,
"id": 1,
"student_id": 1,
"created": "28 May 2024 20:33:46"
}
