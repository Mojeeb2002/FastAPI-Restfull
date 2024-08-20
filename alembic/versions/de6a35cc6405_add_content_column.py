"""add content column

Revision ID: de6a35cc6405
Revises: ef4a2edde05c
Create Date: 2024-08-20 23:42:10.095499

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'de6a35cc6405'
down_revision: Union[str, None] = 'ef4a2edde05c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
