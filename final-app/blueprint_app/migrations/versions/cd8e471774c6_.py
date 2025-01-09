"""empty message

Revision ID: cd8e471774c6
Revises: 
Create Date: 2025-01-09 17:49:02.852260

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd8e471774c6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('pid', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('age', sa.String(), nullable=True),
    sa.Column('job', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('pid')
    )
    op.create_table('todos',
    sa.Column('tid', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('done', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('tid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todos')
    op.drop_table('people')
    # ### end Alembic commands ###