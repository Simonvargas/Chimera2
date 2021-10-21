"""empty message

Revision ID: ae6db96477d8
Revises: 9f40560ad240
Create Date: 2021-10-21 15:35:41.364516

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae6db96477d8'
down_revision = '9f40560ad240'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('projects', 'funding_raised',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('projects', 'backers',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('projects', 'backers',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('projects', 'funding_raised',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
