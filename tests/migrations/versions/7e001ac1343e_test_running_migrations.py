"""test running migrations

Revision ID: 7e001ac1343e
Revises: fa7f5d68dfe4
Create Date: 2023-11-09 02:34:30.979575

"""
from typing import Sequence
from typing import Union

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision: str = "7e001ac1343e"
down_revision: Union[str, None] = "fa7f5d68dfe4"
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
