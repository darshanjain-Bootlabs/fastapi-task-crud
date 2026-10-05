from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Task
from app.schemas import Task as TaskSchema
from app.schemas import TaskCreate, TaskUpdate

app = FastAPI()

@app.get("/")
def read_root():
    return {"Project": "Task manager."}


@app.get("/tasks", response_model=list[TaskSchema])
def get_tasks(db: Session = Depends(get_db)):
    return db.query(Task).all()


@app.post("/tasks/", response_model=TaskSchema, status_code=201)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    db_task = Task(
        title=task.title,
        description=task.description,
        completed=task.completed,
        priority=task.priority,
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


@app.get("/tasks/{task_id}", response_model=TaskSchema)
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.patch("/tasks/{task_id}", response_model=TaskSchema)
def update_task(
    task_id: int, task_update: TaskUpdate, db: Session = Depends(get_db)
):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    for field, value in task_update.model_dump(exclude_unset=True).items():
        setattr(task, field, value)
    db.commit()
    db.refresh(task)
    return task


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()