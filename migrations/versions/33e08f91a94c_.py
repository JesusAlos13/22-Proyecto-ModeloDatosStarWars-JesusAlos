"""empty message

Revision ID: 33e08f91a94c
Revises: f056aa31c462
Create Date: 2025-05-19 09:47:12.141257

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33e08f91a94c'
down_revision = 'f056aa31c462'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('starship',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('model', sa.String(), nullable=False),
    sa.Column('manufacturer', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorites_starship',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('starship_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['starship_id'], ['starship.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'starship_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorites_starship')
    op.drop_table('starship')
    # ### end Alembic commands ###
