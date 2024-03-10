from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from tracker.router import router as tracker_router

tags_metadata = [
    {
        'name': 'tasks',
        'description': 'Tasks ednpoints'
    },
]

origins = [
    'http://localhost',
    'http://localhost:3000',
    'http://localhost:5173',
    'http://localhost:8080',
    'http://178.154.207.253:8000',
    '178.154.207.253:8000',
    'http://178.154.207.253'
]


app = FastAPI(
    title='Test for Ansara',
    description='Tracker for Ansara',
    version='0.0.1',
    openapi_tags=tags_metadata,
)

app.include_router(tracker_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)