"""empty message

Revision ID: cf90799f50d2
Revises: 
Create Date: 2021-11-11 11:05:46.007942

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf90799f50d2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('audience',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('number', sa.Integer(), nullable=True),
    sa.Column('amount_of_places', sa.Integer(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('reservuation_date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=45), nullable=True),
    sa.Column('surname', sa.String(length=45), nullable=True),
    sa.Column('username', sa.String(length=45), nullable=True),
    sa.Column('password', sa.String(length=45), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reservation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=45), nullable=True),
    sa.Column('audience_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['audience_id'], ['audience.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reservation')
    op.drop_table('user')
    op.drop_table('audience')
    # ### end Alembic commands ###
