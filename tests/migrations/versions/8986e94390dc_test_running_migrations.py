"""test running migrations

Revision ID: 8986e94390dc
Revises: a5f7a3c2472d
Create Date: 2023-11-13 03:11:40.580360

"""
from typing import Sequence
from typing import Union

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision: str = "8986e94390dc"
down_revision: Union[str, None] = "a5f7a3c2472d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
