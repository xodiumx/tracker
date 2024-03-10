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
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['GET', 'POST', 'OPTIONS', 'PUT', 'PATCH', 'DELETE'],
    allow_headers=["Content-Type", "Set-Cookie", 
                   "Access-Control-Allow-Headers", 
                   "Access-Control-Allow-Origin",
                   "Authorization"
    ],
)