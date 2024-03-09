from datetime import datetime

from sqlalchemy import Column, Date, Integer, String, Table

from main.db_connect import metadata

tasks = Table(
    'tasks',
    metadata,
    Column('id', Integer, primary_key=True, index=True,),
    Column('name', String(256), nullable=False,),
    Column('state', String(128), nullable=False, default='running'),
    Column(
        'created_at',
        Date,
        default=datetime.now,
    ),
)
