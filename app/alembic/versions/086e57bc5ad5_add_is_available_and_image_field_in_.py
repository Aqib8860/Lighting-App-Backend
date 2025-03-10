"""Add is_available and image field in Product Bulb

Revision ID: 086e57bc5ad5
Revises: 3aae633ed324
Create Date: 2025-02-26 18:10:20.478561

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '086e57bc5ad5'
down_revision: Union[str, None] = '3aae633ed324'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product_bulbs', sa.Column('is_available', sa.Boolean(), nullable=True))
    op.add_column('product_bulbs', sa.Column('image', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product_bulbs', 'image')
    op.drop_column('product_bulbs', 'is_available')
    # ### end Alembic commands ###
