from sqlalchemy import Boolean, Text , Integer, String
from sqlalchemy.orm import mapped_column, Mapped
from app.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(200), index=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    priority: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    completed: Mapped[bool] = mapped_column(Boolean, default=False)

