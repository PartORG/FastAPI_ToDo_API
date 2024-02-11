"""Create phone number for User column

Revision ID: 790af12feaff
Revises: 
Create Date: 2024-02-08 16:24:39.969147

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '790af12feaff'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column('users', 'phone_number')

