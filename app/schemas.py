from pydantic import BaseModel


class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    completed: bool = False
    priority: int = 1


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None
    priority: int | None = None


class Task(BaseModel):
    id: int
    title: str
    description: str | None = None
    completed: bool
    priority: int

    model_config = {"from_attributes": True}