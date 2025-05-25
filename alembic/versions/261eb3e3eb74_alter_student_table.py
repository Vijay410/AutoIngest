"""alter student table

Revision ID: 261eb3e3eb74
Revises: c76a54f10cc0
Create Date: 2025-05-25 21:55:21.523956

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '261eb3e3eb74'
down_revision: Union[str, None] = 'c76a54f10cc0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute(
        """
        ALTER TABLE public."StudentsInfo"
        ADD COLUMN "StudentAdmissionNumber" VARCHAR(100) UNIQUE
        """
    )


def downgrade() -> None:
    """Downgrade schema."""
    pass
