from datetime import datetime

from pydantic import BaseModel


class BaseTaskSchema(BaseModel):
    name: str

    class Config:
        orm_mode = True


class GetTaskSchema(BaseTaskSchema):
    id: int
    state: str
    created_at: str


class CreateTaskSchema(BaseTaskSchema):
    ...
