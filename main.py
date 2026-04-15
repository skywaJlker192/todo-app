import sys

from todo.manager import add, complete, delete, list_tasks

HELP = """
Использование:
  python main.py add <название>   — добавить задачу
  python main.py list             — показать все задачи
  python main.py done <id>        — отметить выполненной
  python main.py delete <id>      — удалить задачу
"""


def main() -> None:
    args = sys.argv[1:]

    if not args:
        print(HELP)
        return

    cmd = args[0]

    if cmd == "add":
        if len(args) < 2:
            print("Укажите название задачи")
            return
        title = " ".join(args[1:])
        task = add(title)
        print(f"Добавлено: [{task['id']}] {task['title']}")

    elif cmd == "list":
        tasks = list_tasks()
        if not tasks:
            print("Задач нет")
            return
        for t in tasks:
            status = "✓" if t["done"] else "○"
            print(f"  {status} [{t['id']}] {t['title']}")

    elif cmd == "done":
        if len(args) < 2:
            print("Укажите id задачи")
            return
        ok = complete(int(args[1]))
        print("Готово!" if ok else "Задача не найдена")

    elif cmd == "delete":
        if len(args) < 2:
            print("Укажите id задачи")
            return
        ok = delete(int(args[1]))
        print("Удалено!" if ok else "Задача не найдена")

    else:
        print(HELP)


if __name__ == "__main__":
    main()

 