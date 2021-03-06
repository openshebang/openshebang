"""empty message

Revision ID: dcc3de959796
Revises: d42300a5fd7a
Create Date: 2021-04-06 12:03:13.576001

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dcc3de959796'
down_revision = 'd42300a5fd7a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dib_settings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('delay', sa.Integer(), nullable=True),
    sa.Column('toptext', sa.String(), nullable=True),
    sa.Column('topimage', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dib_settings')
    # ### end Alembic commands ###
