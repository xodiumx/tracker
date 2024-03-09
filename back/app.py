from fastapi import FastAPI

tags_metadata = [
    {
        'name': 'tasks',
        'description': 'Tasks ednpoints'
    },
]

app = FastAPI(
    title='Test for Ansra',
    description='Tracker for Ansra',
    version='0.0.1',
    openapi_tags=tags_metadata,
)
