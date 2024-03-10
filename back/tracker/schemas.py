from datetime import datetime

from pydantic import BaseModel


class BaseTaskSchema(BaseModel):
    name: str
    time_in_work: int

    class Config:
        orm_mode = True


class GetTaskSchema(BaseTaskSchema):
    id: int
    state: str
    created_at: str


class CreateTaskSchema(BaseTaskSchema):
    ...


class UpdateTaskSchema(BaseTaskSchema):
    ...
