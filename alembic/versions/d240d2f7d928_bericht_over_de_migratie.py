"""Bericht over de migratie

Revision ID: d240d2f7d928
Revises: 
Create Date: 2023-12-22 18:41:11.833342

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd240d2f7d928'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('leerjaar',
    sa.Column('eindjaar', sa.Integer(), nullable=True),
    sa.Column('startjaar', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('leerling',
    sa.Column('kwetsbarejongere', sa.Boolean(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('onderwijsniveau',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('onderwijssoort',
    sa.Column('omschrijving', sa.String(length=80), nullable=True),
    sa.Column('onderwijstype', sa.Enum('VMBO_T', 'VMBO_K', 'VMBO_B', 'HAVO', 'VWO', name='onderwijstype'), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ouder_of_verzorger',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('school',
    sa.Column('naam', sa.String(length=200), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('inschrijving',
    sa.Column('datum', sa.String(), nullable=True),
    sa.Column('school_id', sa.Integer(), nullable=False),
    sa.Column('leerling_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['leerling_id'], ['leerling.id'], ),
    sa.ForeignKeyConstraint(['school_id'], ['school.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_inschrijving_leerling_id'), 'inschrijving', ['leerling_id'], unique=False)
    op.create_index(op.f('ix_inschrijving_school_id'), 'inschrijving', ['school_id'], unique=False)
    op.create_table('koppel_heeft_EAID_CED5C094_5222_4347_9FE1_7D5B2DECA3DD',
    sa.Column('left_id', sa.Integer(), nullable=False),
    sa.Column('right_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['left_id'], ['school.id'], ),
    sa.ForeignKeyConstraint(['right_id'], ['onderwijssoort.id'], ),
    sa.PrimaryKeyConstraint('left_id', 'right_id')
    )
    op.create_table('locatie',
    sa.Column('adres', sa.String(), nullable=True),
    sa.Column('school_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['school_id'], ['school.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_locatie_school_id'), 'locatie', ['school_id'], unique=False)
    op.create_table('onderwijsloopbaan',
    sa.Column('leerling_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['leerling_id'], ['leerling.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_onderwijsloopbaan_leerling_id'), 'onderwijsloopbaan', ['leerling_id'], unique=False)
    op.create_table('startkwalificatie',
    sa.Column('datumbehaald', sa.String(), nullable=True),
    sa.Column('leerling_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['leerling_id'], ['leerling.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_startkwalificatie_leerling_id'), 'startkwalificatie', ['leerling_id'], unique=False)
    op.create_table('uitschrijving',
    sa.Column('datum', sa.String(), nullable=True),
    sa.Column('diplomabehaald', sa.Boolean(), nullable=True),
    sa.Column('leerling_id', sa.Integer(), nullable=False),
    sa.Column('school_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['leerling_id'], ['leerling.id'], ),
    sa.ForeignKeyConstraint(['school_id'], ['school.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_uitschrijving_leerling_id'), 'uitschrijving', ['leerling_id'], unique=False)
    op.create_index(op.f('ix_uitschrijving_school_id'), 'uitschrijving', ['school_id'], unique=False)
    op.create_table('koppel_kent_EAID_FA07FA3D_3EC3_450e_8FE0_766875D7CC5F',
    sa.Column('left_id', sa.Integer(), nullable=False),
    sa.Column('right_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['left_id'], ['school.id'], ),
    sa.ForeignKeyConstraint(['right_id'], ['onderwijsloopbaan.id'], ),
    sa.PrimaryKeyConstraint('left_id', 'right_id')
    )
    op.create_table('loopbaanstap',
    sa.Column('klas', sa.Integer(), nullable=True),
    sa.Column('onderwijstype', sa.Enum('VMBO_T', 'VMBO_K', 'VMBO_B', 'HAVO', 'VWO', name='onderwijstype'), nullable=True),
    sa.Column('schooljaar', sa.String(), nullable=True),
    sa.Column('onderwijsloopbaan_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['onderwijsloopbaan_id'], ['onderwijsloopbaan.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_loopbaanstap_onderwijsloopbaan_id'), 'loopbaanstap', ['onderwijsloopbaan_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_loopbaanstap_onderwijsloopbaan_id'), table_name='loopbaanstap')
    op.drop_table('loopbaanstap')
    op.drop_table('koppel_kent_EAID_FA07FA3D_3EC3_450e_8FE0_766875D7CC5F')
    op.drop_index(op.f('ix_uitschrijving_school_id'), table_name='uitschrijving')
    op.drop_index(op.f('ix_uitschrijving_leerling_id'), table_name='uitschrijving')
    op.drop_table('uitschrijving')
    op.drop_index(op.f('ix_startkwalificatie_leerling_id'), table_name='startkwalificatie')
    op.drop_table('startkwalificatie')
    op.drop_index(op.f('ix_onderwijsloopbaan_leerling_id'), table_name='onderwijsloopbaan')
    op.drop_table('onderwijsloopbaan')
    op.drop_index(op.f('ix_locatie_school_id'), table_name='locatie')
    op.drop_table('locatie')
    op.drop_table('koppel_heeft_EAID_CED5C094_5222_4347_9FE1_7D5B2DECA3DD')
    op.drop_index(op.f('ix_inschrijving_school_id'), table_name='inschrijving')
    op.drop_index(op.f('ix_inschrijving_leerling_id'), table_name='inschrijving')
    op.drop_table('inschrijving')
    op.drop_table('school')
    op.drop_table('ouder_of_verzorger')
    op.drop_table('onderwijssoort')
    op.drop_table('onderwijsniveau')
    op.drop_table('leerling')
    op.drop_table('leerjaar')
    # ### end Alembic commands ###
