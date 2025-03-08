"""Add height column

Revision ID: 33cc176431b9
Revises: 4701382538bc
Create Date: 2025-02-26 17:52:42.214052

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '33cc176431b9'
down_revision: Union[str, None] = '4701382538bc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('test_field', sa.String(), nullable=True))
    op.create_index(op.f('ix_products_test_field'), 'products', ['test_field'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_products_test_field'), table_name='products')
    op.drop_column('products', 'test_field')
    # ### end Alembic commands ###
