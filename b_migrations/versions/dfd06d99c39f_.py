"""empty message

Revision ID: dfd06d99c39f
Revises: 3c78137ff935
Create Date: 2021-04-09 14:19:55.832258

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dfd06d99c39f'
down_revision = '3c78137ff935'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('dib_entries', sa.Column('image', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('dib_entries', 'image')
    # ### end Alembic commands ###
