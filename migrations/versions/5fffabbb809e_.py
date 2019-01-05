"""empty message

Revision ID: 5fffabbb809e
Revises: 2b89a4afd0d0
Create Date: 2018-09-23 18:00:12.182333

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5fffabbb809e'
down_revision = '2b89a4afd0d0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('album_comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('album_id', sa.Integer(), nullable=True),
    sa.Column('author_id', sa.String(length=100), nullable=True),
    sa.Column('origin_comment_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['album_id'], ['album.id'], ),
    sa.ForeignKeyConstraint(['author_id'], ['front_user.id'], ),
    sa.ForeignKeyConstraint(['origin_comment_id'], ['album_comment.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('album_star',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('album_id', sa.Integer(), nullable=True),
    sa.Column('author_id', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['album_id'], ['album.id'], ),
    sa.ForeignKeyConstraint(['author_id'], ['front_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('album_star')
    op.drop_table('album_comment')
    # ### end Alembic commands ###
