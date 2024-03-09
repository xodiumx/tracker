from fastapi import Depends
from sqlalchemy import delete, insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from main.db_connect import get_async_session

from .tables import tasks
from .schemas import CreateTaskSchema


class TaskService:
    
    def __init__(
            self,
            session: AsyncSession = Depends(get_async_session)) -> None:
        """Creating a new session."""
        self.session = session

    async def get_all_tasks(self) -> list:
        """Get all tasks from db."""
        query = select(tasks)
        response = await self.session.execute(query)
        return response.all()
    
    async def create_task(
            self,
            data: CreateTaskSchema) -> None:
        """Create a new task."""
        new_task = data.dict()
        statement = insert(tasks).values(**new_task)
        await self.session.execute(statement)
        await self.session.commit()
        return new_task
    
    async def delete_task(self, task_id: int) -> None:
        """
        Delete task function
          - Filter the post by id
        """
        query = (
            delete(tasks)
            .filter_by(id=task_id)
        )
        await self.session.execute(query)
        await self.session.commit()
