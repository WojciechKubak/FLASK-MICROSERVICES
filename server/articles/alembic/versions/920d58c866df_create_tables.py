"""create tables

Revision ID: 920d58c866df
Revises: 
Create Date: 2023-10-14 16:52:33.274277

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '920d58c866df'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'categories',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('description', sa.String()),
        sa.Column('created_at', sa.DateTime),
        sa.Column('updated_at', sa.DateTime),
    )
    op.create_table(
        'articles',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('content', sa.String(10000)),
        sa.Column('publication_date', sa.DateTime),
        sa.Column('category_id', sa.Integer, sa.ForeignKey('categories.id')),
        sa.Column('created_at', sa.DateTime),
        sa.Column('updated_at', sa.DateTime),
    )
    op.create_table(
        'tags',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime),
    )
    op.create_table(
        'articles_tags',
        sa.Column('article_id', sa.Integer, sa.ForeignKey('articles.id')),
        sa.Column('tag_id', sa.Integer, sa.ForeignKey('tags.id')),
        sa.Column('created_at', sa.DateTime),
    )


def downgrade() -> None:
    op.drop_table('articles_tags')
    op.drop_table('articles')
    op.drop_table('tags')
    op.drop_table('categories')
