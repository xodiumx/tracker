from datetime import datetime

from sqlalchemy import Column, Integer, String, Table

from main.db_connect import metadata

tasks = Table(
    'tasks',
    metadata,
    Column('id', Integer, primary_key=True, index=True,),
    Column('name', String(256), nullable=False,),
    Column('state', String(128), nullable=False, default='running'),
    Column(
        'created_at',
        String,
        nullable=False,
        default=str(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'))
    ),
    Column(
        'time_in_work',
        Integer,
        nullable=False,
    ),
)
