"""Renaming students to scholars

Revision ID: 1a9445983a24
Revises: 791279dd0760
Create Date: 2023-12-06 07:44:47.673072

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a9445983a24'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
