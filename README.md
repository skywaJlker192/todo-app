# Todo App

Простой CLI-менеджер задач на Python.

## Возможности

- Добавление задач
- Просмотр списка задач
- Отметка выполненных задач
- Удаление задач
- Сохранение в JSON-файл

## Запуск

### Локально

```bash
pip install -r requirements.txt
python main.py list
python main.py add "Сделать домашку"
python main.py done 1
python main.py delete 1
```

### Docker

```bash
docker build -t todo-app .
docker run --rm todo-app
```

### Docker Compose

```bash
docker compose up       # запустить
docker compose down     # остановить
```

## Инструменты качества кода

- **black** — форматирование
- **ruff** — линтер
- **pre-commit** — автоматические проверки перед коммитом

### Установка pre-commit hooks

```bash
pip install pre-commit
pre-commit install
```

После этого перед каждым `git commit` автоматически запускаются black и ruff.

## Структура проекта

```
todo-app/
├── main.py              # точка входа (CLI)
├── todo/
│   ├── manager.py       # логика работы с задачами
│   └── storage.py       # чтение/запись JSON
├── requirements.txt
├── pyproject.toml       # конфигурация black и ruff
├── .pre-commit-config.yaml
├── Dockerfile
├── docker-compose.yml
├── .gitignore
└── .dockerignore
```
