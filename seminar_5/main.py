"""
Необходимо создать API для управления списком задач. Каждая задача должна содержать заголовок и описание. Для каждой задачи должна быть возможность указать статус (выполнена/не выполнена).

API должен содержать следующие конечные точки:
— GET /tasks — возвращает список всех задач.
— GET /tasks/{id} — возвращает задачу с указанным идентификатором.
— POST /tasks — добавляет новую задачу.
— PUT /tasks/{id} — обновляет задачу с указанным идентификатором.
— DELETE /tasks/{id} — удаляет задачу с указанным идентификатором.

Для каждой конечной точки необходимо проводить валидацию данных запроса и ответа. Для этого использовать библиотеку Pydantic.
"""
from pydantic import BaseModel
from fastapi import FastAPI
from typing import Dict, List
from collections import defaultdict


app = FastAPI()


class Task(BaseModel):
    id: int
    title: str
    description: str
    status: bool = False


tasks_db: Dict[int, Task] = defaultdict()


@app.get("/tasks")
async def read_tasks(skip: int = 0, limit: int = 100):
    return list(tasks_db.values())[skip: skip + limit]


@app.get("/tasks/{task_id}", response_model=Task)
async def read_task(task_id: int):
    return tasks_db[task_id]


@app.post("/tasks", response_model=Task)
async def create_task(task: Task):
    task_id = len(tasks_db) + 1
    db_task = Task(id=task_id, **task.dict())
    tasks_db[task_id] = db_task
    return db_task


@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task: Task):
    db_task = tasks_db[task_id]
    for field, value in task.dict(exclude_unset=True).items():
        setattr(db_task, field, value)
    return db_task


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    del tasks_db[task_id]
    return {"result": "success"}