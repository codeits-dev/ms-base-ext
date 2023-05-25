"""empty message

Revision ID: 9508b65f6c18
Revises: 6d2fd217001a
Create Date: 2023-04-14 21:06:38.173961

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9508b65f6c18'
down_revision = '6d2fd217001a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('person', sa.Column('lastname', sa.String(), nullable=False))
    op.add_column('person', sa.Column('birthdate', sa.Date(), nullable=False))
    # ### end Alembic commands ###
    
    


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('person', 'birthdate')
    op.drop_column('person', 'lastname')
    # ### end Alembic commands ###
