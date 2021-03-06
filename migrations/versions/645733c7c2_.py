# flake8: noqa
"""empty message

Revision ID: 645733c7c2
Revises: 8914b3f843
Create Date: 2015-11-20 15:36:27.537882

"""

# revision identifiers, used by Alembic.
revision = '645733c7c2'
down_revision = '8914b3f843'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('borrower',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('forename', sa.String(), nullable=False),
    sa.Column('middlename', sa.String(), nullable=True),
    sa.Column('surname', sa.String(), nullable=False),
    sa.Column('dob', sa.String(), nullable=False),
    sa.Column('gender', sa.String(), nullable=True),
    sa.Column('phonenumber', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('borrower')
    ### end Alembic commands ###
