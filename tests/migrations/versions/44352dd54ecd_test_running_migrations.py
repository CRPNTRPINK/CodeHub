"""test running migrations

Revision ID: 44352dd54ecd
Revises: 6ba634c3e5bb
Create Date: 2023-11-13 03:22:24.810941

"""
from typing import Sequence
from typing import Union

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision: str = "44352dd54ecd"
down_revision: Union[str, None] = "6ba634c3e5bb"
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
