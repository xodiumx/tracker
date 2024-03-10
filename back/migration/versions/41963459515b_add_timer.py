"""add timer

Revision ID: 41963459515b
Revises: 51b17bb6196b
Create Date: 2024-03-10 15:29:40.586778

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41963459515b'
down_revision = '51b17bb6196b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('time_in_work', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks', 'time_in_work')
    # ### end Alembic commands ###
