"""empty message

Revision ID: d9af000dffca
Revises: 
Create Date: 2022-09-05 15:51:34.000774

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9af000dffca'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blacklist_tokens',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(length=500), nullable=False),
    sa.Column('blacklisted_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('stac_ingestion_status',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('newly_stored_collections_count', sa.Integer(), nullable=True),
    sa.Column('newly_stored_collections', sa.Text(), nullable=True),
    sa.Column('updated_collections_count', sa.Integer(), nullable=True),
    sa.Column('updated_collections', sa.Text(), nullable=True),
    sa.Column('newly_stored_item_count', sa.Integer(), nullable=True),
    sa.Column('updated_items_count', sa.Integer(), nullable=True),
    sa.Column('already_stored_items_count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('registered_on', sa.DateTime(), nullable=False),
    sa.Column('admin', sa.Boolean(), nullable=False),
    sa.Column('public_id', sa.String(length=100), nullable=True),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('password_hash', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('public_id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('stac_ingestion_status')
    op.drop_table('blacklist_tokens')
    # ### end Alembic commands ###
