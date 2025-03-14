"""empty message

Revision ID: af3ef2ef6646
Revises: 71f85960fd9e
Create Date: 2025-03-12 16:50:59.738756

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af3ef2ef6646'
down_revision = '71f85960fd9e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('hoteles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=120), nullable=False),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('nombre')
    )
    op.create_table('room',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nombre')
    )
    op.create_table('theme',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nombre')
    )
    op.create_table('branches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=120), nullable=False),
    sa.Column('direccion', sa.String(length=120), nullable=False),
    sa.Column('longitud', sa.Float(), nullable=False),
    sa.Column('latitud', sa.Float(), nullable=False),
    sa.Column('hotel_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['hotel_id'], ['hoteles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('hoteltheme',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_hoteles', sa.Integer(), nullable=True),
    sa.Column('id_theme', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_hoteles'], ['hoteles.id'], ),
    sa.ForeignKeyConstraint(['id_theme'], ['theme.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('maintenance',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=120), nullable=False),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('hotel_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['hotel_id'], ['hoteles.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('housekeeper',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=120), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('id_branche', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_branche'], ['branches.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('nombre')
    )
    op.create_table('housekeepertask',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=120), nullable=False),
    sa.Column('photo', sa.String(length=120), nullable=False),
    sa.Column('condition', sa.String(length=80), nullable=False),
    sa.Column('assignment_date', sa.String(length=80), nullable=False),
    sa.Column('submission_date', sa.String(length=80), nullable=False),
    sa.Column('id_room', sa.Integer(), nullable=True),
    sa.Column('id_housekeeper', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_housekeeper'], ['housekeeper.id'], ),
    sa.ForeignKeyConstraint(['id_room'], ['room.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nombre'),
    sa.UniqueConstraint('photo')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('theme', sa.String(length=120), nullable=False))
        batch_op.create_unique_constraint(None, ['theme'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('theme')

    op.drop_table('housekeepertask')
    op.drop_table('housekeeper')
    op.drop_table('maintenance')
    op.drop_table('hoteltheme')
    op.drop_table('branches')
    op.drop_table('theme')
    op.drop_table('room')
    op.drop_table('hoteles')
    op.drop_table('category')
    # ### end Alembic commands ###
