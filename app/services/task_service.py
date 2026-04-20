from typing import Optional
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.task import Task
from app.repositories import task_repository


def create_task(db: Session, data: dict) -> Task:
    return task_repository.create_task(db, data)


def get_task(db: Session, task_id: int) -> Task:
    task = task_repository.get_task_by_id(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


def list_tasks(db: Session, status: Optional[str] = None) -> list[Task]:
    return task_repository.get_all_tasks(db, status)


def update_task(db: Session, task_id: int, data: dict) -> Task:
    task = get_task(db, task_id)
    return task_repository.update_task(db, task, data)


def delete_task(db: Session, task_id: int) -> None:
    task = get_task(db, task_id)
    task_repository.delete_task(db, task)
