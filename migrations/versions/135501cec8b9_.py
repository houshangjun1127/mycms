"""empty message

Revision ID: 135501cec8b9
Revises: 8e32ec69e951
Create Date: 2018-09-16 15:45:36.393145

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '135501cec8b9'
down_revision = '8e32ec69e951'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('group', sa.Column('desc', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('group', 'desc')
    # ### end Alembic commands ###
