"""empty message

Revision ID: 9995990e1ef3
Revises: 056192e74bdd
Create Date: 2017-06-11 12:25:28.754295

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9995990e1ef3'
down_revision = '056192e74bdd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('projectitems',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account_id', sa.Integer(), nullable=True),
    sa.Column('workitem_id', sa.Integer(), nullable=True),
    sa.Column('start_date', sa.Date(), nullable=True),
    sa.Column('end_date', sa.Date(), nullable=True),
    sa.Column('more_details', sa.String(length=400), nullable=True),
    sa.ForeignKeyConstraint(['account_id'], ['employees.id'], ),
    sa.ForeignKeyConstraint(['workitem_id'], ['workitems.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('projectitems')
    # ### end Alembic commands ###