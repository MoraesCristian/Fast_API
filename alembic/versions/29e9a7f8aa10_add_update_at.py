"""add update_at

Revision ID: 29e9a7f8aa10
Revises: 9d7a9fde0f6b
Create Date: 2024-08-01 20:46:16.077621

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '29e9a7f8aa10'
down_revision: Union[str, None] = '9d7a9fde0f6b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        'users',
        sa.Column(
            'updated_at',
            sa.DateTime(),
            server_default=sa.text('(CURRENT_TIMESTAMP)'),
            nullable=False,
        ),
    )
    # ### end Alembic commands ###
    op.execute("""
        CREATE OR REPLACE FUNCTION update_user_updated_at()
        RETURNS TRIGGER AS $$
        BEGIN
            NEW.updated_at = CURRENT_TIMESTAMP;
            RETURN NEW;
        END;
        $$ LANGUAGE plpgsql;
        """)

    op.execute("""
        CREATE TRIGGER update_user_updated_at
        BEFORE UPDATE ON users
        FOR EACH ROW
        EXECUTE FUNCTION update_user_updated_at();
        """)


def downgrade() -> None:
    # Remove o trigger
    op.execute("DROP TRIGGER IF EXISTS update_user_updated_at ON users;")

    # Remove a função
    op.execute("DROP FUNCTION IF EXISTS update_user_updated_at;")
    op.drop_column('users', 'updated_at')
    # ### end Alembic commands ###
