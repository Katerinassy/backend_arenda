from pydantic import BaseModel, EmailStr, HttpUrl
from datetime import datetime
from typing import Optional, List
from fastapi import FastAPI, HTTPException
from uuid import uuid4, UUID

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    priority: int
    deadline: Optional[datetime] = None

class TaskCreate(TaskBase):
    pass

class TaskShort(TaskBase):
    id: UUID
    is_completed: bool

class TaskFull(TaskShort):
    created_at: datetime
    updated_at: Optional[datetime] = None

app = FastAPI()

# Хранилище задач
tasks_db: List[TaskFull] = []

@app.post("/tasks", response_model=TaskShort)
def create_task(task: TaskCreate):
    task_full = TaskFull(
        id=uuid4(),
        is_completed=False,
        created_at=datetime.now(),
        updated_at=None,
        title=task.title,
        description=task.description,
        priority=task.priority,
        deadline=task.deadline,
    )
    tasks_db.append(task_full)
    return task_full

@app.get("/tasks", response_model=List[TaskShort])
def list_tasks():
    return tasks_db

@app.get("/tasks/{task_id}", response_model=TaskFull)
def get_task(task_id: UUID):
    for task in tasks_db:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Задача не найдена")
