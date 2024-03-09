from fastapi import FastAPI

from tracker.router import router as tracker_router

tags_metadata = [
    {
        'name': 'tasks',
        'description': 'Tasks ednpoints'
    },
]

app = FastAPI(
    title='Test for Ansara',
    description='Tracker for Ansara',
    version='0.0.1',
    openapi_tags=tags_metadata,
)

app.include_router(tracker_router)
