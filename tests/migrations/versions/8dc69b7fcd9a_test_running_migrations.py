"""test running migrations

Revision ID: 8dc69b7fcd9a
Revises: a58e23ec7b72
Create Date: 2023-11-13 00:51:11.196039

"""
from typing import Sequence
from typing import Union

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision: str = "8dc69b7fcd9a"
down_revision: Union[str, None] = "a58e23ec7b72"
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
