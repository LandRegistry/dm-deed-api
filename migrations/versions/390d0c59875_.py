# flake8: noqa
"""empty message

Revision ID: 390d0c59875
Revises: 610e8a67d8
Create Date: 2016-01-12 10:54:59.254585

"""

# revision identifiers, used by Alembic.
revision = '390d0c59875'
down_revision = '610e8a67d8'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('borrower', sa.Column('deed_token', sa.String(), nullable=False))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('borrower', 'deed_id')
    ### end Alembic commands ###
