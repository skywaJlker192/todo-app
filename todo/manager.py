from todo.storage import load, save


def add(title: str) -> dict:
    tasks = load()
    task = {"id": len(tasks) + 1, "title": title, "done": False}
    tasks.append(task)
    save(tasks)
    return task


def list_tasks() -> list[dict]:
    return load()


def complete(task_id: int) -> bool:
    tasks = load()
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save(tasks)
            return True
    return False


def delete(task_id: int) -> bool:
    tasks = load()
    new_tasks = [t for t in tasks if t["id"] != task_id]
    if len(new_tasks) == len(tasks):
        return False
    save(new_tasks)
    return True
