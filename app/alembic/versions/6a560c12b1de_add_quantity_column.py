"""Add quantity column

Revision ID: 6a560c12b1de
Revises: dad02ec3d0d4
Create Date: 2025-02-28 20:38:50.759806

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6a560c12b1de'
down_revision: Union[str, None] = 'dad02ec3d0d4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('quantity', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('products', 'quantity')
    # ### end Alembic commands ###
