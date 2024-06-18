"""Adicionar colunas exercicios, dificuldades, divertido

Revision ID: 1edc014ee4b6
Revises: f34171f817da
Create Date: 2024-06-18 16:58:20.859768

"""
from alembic import op
import sqlalchemy as sa


# Use o seu número de revisão específico
revision = '1edc014ee4b6'
down_revision = 'f34171f817da'
branch_labels = None
depends_on = None


def upgrade():
    # Adicione colunas com valor padrão NULL
    op.add_column('feedback', sa.Column('exercicios', sa.String(length=10), nullable=True))
    op.add_column('feedback', sa.Column('dificuldades', sa.String(length=255), nullable=True))
    op.add_column('feedback', sa.Column('divertido', sa.String(length=5), nullable=True))

    # Opção alternativa se o SQLite não suportar adição de colunas com valor padrão NULL
    # op.add_column('feedback', sa.Column('exercicios', sa.String(length=10), server_default=''))
    # op.add_column('feedback', sa.Column('dificuldades', sa.String(length=255), server_default=''))
    # op.add_column('feedback', sa.Column('divertido', sa.String(length=5), server_default=''))


def downgrade():
    op.drop_column('feedback', 'exercicios')
    op.drop_column('feedback', 'dificuldades')
    op.drop_column('feedback', 'divertido')


    # ### end Alembic commands ###
