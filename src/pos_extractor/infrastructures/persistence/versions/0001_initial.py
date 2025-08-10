# src/pos_extractor/infrastructures/persistence/db/versions/0001_initial.py
# migration script for initial database schema.

"""initial tables

Revision ID: 0001_initial
Revises: 
Create Date: 2025-08-09 00:00:00
"""
from alembic import op
import sqlalchemy as sa
revision = '0001_initial'
down_revision = None
branch_labels = None
depends_on = None
def upgrade() -> None:
    op.create_table('jobs',
        sa.Column('id', sa.String(length=36), primary_key=True),
        sa.Column('name', sa.String(length=200), nullable=False, server_default=''),
        sa.Column('status', sa.String(length=20), nullable=False, server_default='SUBMITTED'),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.Column('params_json', sa.JSON(), nullable=False, server_default='{}'),
    )
    op.create_table('job_steps',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('job_id', sa.String(length=36), sa.ForeignKey('jobs.id', ondelete='CASCADE')),
        sa.Column('component', sa.String(length=50), nullable=False),
        sa.Column('status', sa.String(length=20), nullable=False, server_default='PENDING'),
        sa.Column('started_at', sa.DateTime(), nullable=True),
        sa.Column('finished_at', sa.DateTime(), nullable=True),
        sa.Column('metrics_json', sa.JSON(), nullable=False, server_default='{}'),
        sa.Column('error_json', sa.JSON(), nullable=False, server_default='{}'),
    )
    op.create_table('artifacts',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('job_id', sa.String(length=36), sa.ForeignKey('jobs.id', ondelete='CASCADE')),
        sa.Column('kind', sa.String(length=50), nullable=False),
        sa.Column('path', sa.Text(), nullable=False),
        sa.Column('meta_json', sa.JSON(), nullable=False, server_default='{}'),
    )
def downgrade() -> None:
    op.drop_table('artifacts')
    op.drop_table('job_steps')
    op.drop_table('jobs')
