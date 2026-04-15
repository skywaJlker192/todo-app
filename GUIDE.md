# ГАЙД: команды Git + отчёт

## Шаг 1. Инициализация

```bash
cd todo-app
git init
git config user.name "Твоё Имя"
git config user.email "почта@example.com"
```

## Шаг 2. Первый коммит (структура проекта)

```bash
git add .gitignore README.md requirements.txt pyproject.toml
git commit -m "init: add project structure and config files"
```

## Шаг 3. Коммит основного кода (ветка main)

```bash
git add todo/ main.py
git commit -m "feat: add todo CLI with add/list/done/delete commands"
```

## Шаг 4. Ветка feature/docker

```bash
git checkout -b feature/docker
git add Dockerfile .dockerignore docker-compose.yml
git commit -m "feat: add Dockerfile and docker-compose.yml"
# Обнови README
git add README.md
git commit -m "docs: add Docker launch instructions to README"
git checkout main
git merge feature/docker
```

## Шаг 5. Ветка feature/pre-commit

```bash
git checkout -b feature/pre-commit
git add .pre-commit-config.yaml
git commit -m "chore: add pre-commit config with black and ruff hooks"
# Устанавливаем хуки локально
pip install pre-commit
pre-commit install
git checkout main
git merge feature/pre-commit
```

## Шаг 6. Pull Request (через GitHub)

1. Запушить ветку: `git push origin feature/docker`
2. На GitHub → New Pull Request → feature/docker → main
3. Добавить описание, создать PR, смёрджить

## Шаг 7. Публикация на GitHub

```bash
git remote add origin https://github.com/ТВО_ЮЗЕ/todo-app.git
git branch -M main
git push -u origin main
```

---

## Краткий отчёт

### Проект
**Todo App** — консольный менеджер задач на Python.

Позволяет добавлять задачи, просматривать список, отмечать выполненные и удалять.
Данные хранятся в `tasks.json`.

### Стек
- Python 3.11
- Docker / Docker Compose
- black, ruff, pre-commit

### Структура репозитория
- `main.py` — точка входа, CLI
- `todo/manager.py` — бизнес-логика
- `todo/storage.py` — работа с JSON
- `Dockerfile` + `docker-compose.yml` — контейнеризация
- `.pre-commit-config.yaml` — автопроверки перед коммитом

### История коммитов (минимум 6)
1. `init: add project structure and config files`
2. `feat: add todo CLI with add/list/done/delete commands`
3. `feat: add Dockerfile and docker-compose.yml`
4. `docs: add Docker launch instructions to README`
5. `chore: add pre-commit config with black and ruff hooks`
6. `fix: sort imports in main.py` (или любой следующий)

### Ветки
- `main` — основная
- `feature/docker` — добавление Docker-файлов
- `feature/pre-commit` — настройка pre-commit

### Pull Request
Создан из `feature/docker` → `main` после добавления Docker-конфига.

---

## GitHub Projects — задачи (минимум 6)

| # | Название | Описание | Исполнитель | Статус | Priority | Start Date | End Date | Estimate |
|---|----------|----------|-------------|--------|----------|------------|----------|----------|
| 1 | Создать структуру проекта | Инициализировать репозиторий, добавить папки и файлы | @ты | Completed | High | - | - | 1h |
| 2 | Реализовать CLI команды | add, list, done, delete | @ты | Completed | High | - | - | 2h |
| 3 | Настроить хранилище JSON | Модуль storage.py для сохранения задач | @ты | Completed | Medium | - | - | 1h |
| 4 | Добавить Docker | Dockerfile и docker-compose.yml | @ты | Completed | Medium | - | - | 1h |
| 5 | Настроить black + ruff | Форматтер и линтер | @ты | Completed | Low | - | - | 30m |
| 6 | Подключить pre-commit | .pre-commit-config.yaml, установить hooks | @ты | Completed | Low | - | - | 30m |

**Представления в GitHub Projects:**
- **Table** — все задачи с полями
- **Board** — Kanban по статусам (Proposed / Active / Resolved / Completed)
- **Roadmap** — задачи по датам

---

## Запуск pre-commit вручную

```bash
pre-commit run --all-files
```

Если есть ошибки — black их исправит сам, ruff покажет что нужно починить.
После исправления повторить `git commit`.
