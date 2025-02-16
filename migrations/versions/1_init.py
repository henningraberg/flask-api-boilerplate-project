"""init

Revision ID: 1_init
Revises:
Create Date:

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1_init'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'boiler_plate_object_1',
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    )

    op.create_table(
        'boiler_plate_object_2',
        sa.Column('parent_id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
        sa.Column('name', sa.Text(), nullable=False),
        sa.ForeignKeyConstraint(
            ['parent_id'],
            ['boiler_plate_object_1.id'],
        ),
    )


def downgrade():
    op.drop_table('boiler_plate_object_1')
    op.drop_table('boiler_plate_object_2')
