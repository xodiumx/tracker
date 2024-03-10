from fastapi import APIRouter, Depends

from .services import TaskService
from .schemas import GetTaskSchema, CreateTaskSchema, UpdateTaskSchema

router = APIRouter(
    prefix='/tasks',
    tags=['tasks']
)


@router.get('', response_model=list[GetTaskSchema])
async def get_all_tasks(
        service: TaskService = Depends(),
    ):
    """Get all tasks."""
    return await service.get_all_tasks()


@router.post('', response_model=CreateTaskSchema)
async def create_task(
        data: CreateTaskSchema,
        service: TaskService = Depends()) -> CreateTaskSchema:
    """Task creation."""
    return await service.create_task(data=data)


@router.patch('/{task_id}')
async def update_task(
        task_id: int,
        data: UpdateTaskSchema,
        service: TaskService = Depends()) -> str:
    """Task update"""
    await service.update_post(
        task_id=task_id,
        data=data
    )
    return 'Task updated successfully'


@router.delete('/{post_id}')
async def delete_task(
        task_id: int,
        service: TaskService = Depends()) -> str:
    """Post removal"""
    await service.delete_task(task_id=task_id)
    return 'Task deleted successfully'
