"""Renaming students to scholars

Revision ID: fdc116512e45
Revises: 791279dd0760
Create Date: 2025-04-22 13:05:33.966101

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fdc116512e45'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
