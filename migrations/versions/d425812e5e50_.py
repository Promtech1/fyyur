"""empty message

Revision ID: d425812e5e50
Revises: d1fc1378e9cf
Create Date: 2022-08-19 21:26:56.976610

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd425812e5e50'
down_revision = 'd1fc1378e9cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artist', sa.Column('website', sa.String(length=120), nullable=True))
    op.add_column('venue', sa.Column('genres', sa.String(length=300), nullable=False))
    op.add_column('venue', sa.Column('website', sa.String(length=120), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venue', 'website')
    op.drop_column('venue', 'genres')
    op.drop_column('artist', 'website')
    # ### end Alembic commands ###
