from fastapi import FastAPI

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
