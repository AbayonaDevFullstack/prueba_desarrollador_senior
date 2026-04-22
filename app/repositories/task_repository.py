from typing import Optional
from sqlalchemy.orm import Session
from app.models.task import Task


def create_task(db: Session, data: dict) -> Task:
    task = Task(**data)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def get_task_by_id(db: Session, task_id: int) -> Optional[Task]:
    return db.query(Task).filter(Task.id == task_id).first()


def get_all_tasks(db: Session, status: Optional[str] = None) -> list[Task]:
    query = db.query(Task)
    if status is not None:
        query = query.filter(Task.status == status)
    return query.all()


def update_task(db: Session, task: Task, data: dict) -> Task:
    for field, value in data.items():
        setattr(task, field, value)
    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, task: Task) -> None:
    db.delete(task)
    db.commit()
