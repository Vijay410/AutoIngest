"""create student performance table

Revision ID: d59cddaffaf5
Revises: 
Create Date: 2025-05-11 16:17:22.026628

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd59cddaffaf5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        CREATE TABLE public."Students" (
            "Id" SERIAL PRIMARY KEY,
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
