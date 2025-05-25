"""create_student_table

Revision ID: c76a54f10cc0
Revises: d59cddaffaf5
Create Date: 2025-05-25 19:42:25.810684

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c76a54f10cc0'
down_revision: Union[str, None] = 'd59cddaffaf5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        DROP TABLE IF EXISTS public."Students";
        CREATE TABLE public."StudentsInfo" (
            "StudentID" SERIAL PRIMARY KEY,
            "Gender" VARCHAR(10),
            "RaceOREthnicity" TEXT,
            "ParentalLevelOfEducation" TEXT,
            "Lunch" VARCHAR(20),
            "TestPreparationCource" VARCHAR(50),
            "MathScore" INTEGER,
            "ReadingScore" INTEGER,
            "WritingScore" INTEGER
        );
        """
    )


def downgrade() -> None:
    """Downgrade schema."""
    pass
