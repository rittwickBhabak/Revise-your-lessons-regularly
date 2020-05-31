"""end date column added to task model

Revision ID: 9d7c2402b124
Revises: 
Create Date: 2020-05-31 10:56:22.357112

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d7c2402b124'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('revisions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.Column('taskId', sa.Integer(), nullable=True),
    sa.Column('day', sa.Integer(), nullable=True),
    sa.Column('month', sa.Integer(), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tasks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('taskName', sa.String(), nullable=True),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.Column('startDay', sa.Integer(), nullable=True),
    sa.Column('startMonth', sa.Integer(), nullable=True),
    sa.Column('startYear', sa.Integer(), nullable=True),
    sa.Column('endDay', sa.Integer(), nullable=True),
    sa.Column('endMonth', sa.Integer(), nullable=True),
    sa.Column('endYear', sa.Integer(), nullable=True),
    sa.Column('repetationList', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('password_hash', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('tasks')
    op.drop_table('revisions')
    # ### end Alembic commands ###