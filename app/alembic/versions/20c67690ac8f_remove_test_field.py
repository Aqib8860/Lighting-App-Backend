"""remove test field

Revision ID: 20c67690ac8f
Revises: 33cc176431b9
Create Date: 2025-02-26 17:53:56.578146

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '20c67690ac8f'
down_revision: Union[str, None] = '33cc176431b9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_products_test_field', table_name='products')
    op.drop_column('products', 'test_field')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('test_field', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.create_index('ix_products_test_field', 'products', ['test_field'], unique=False)
    # ### end Alembic commands ###
