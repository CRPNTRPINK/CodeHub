"""test running migrations

Revision ID: 7f0f3ca03e38
Revises: 7697bf9cb390
Create Date: 2023-11-13 00:38:24.427677

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7f0f3ca03e38'
down_revision: Union[str, None] = '7697bf9cb390'
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