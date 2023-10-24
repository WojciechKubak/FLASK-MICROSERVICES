from sqlalchemy import Integer, String, DateTime, ForeignKey, func, Table, Column
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from typing import Any

Base = declarative_base()


articles_tags = Table(
    'articles_tags',
    Base.metadata,
    Column('id', Integer(), primary_key=True),
    Column('article_id', Integer(), ForeignKey('articles.id')),
    Column('tag_id', Integer(), ForeignKey('tags.id')),
)


class ArticleEntity(Base):

    __tablename__ = 'articles'

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    title: Mapped[str] = mapped_column(String(), nullable=True)
    content: Mapped[str] = mapped_column(String(10000))
    publication_date: Mapped[datetime] = mapped_column(DateTime)
    category_id: Mapped[int] = mapped_column(Integer(), ForeignKey('categories.id'))
    created_at: Mapped[datetime] = mapped_column(default=func.utc_timestamp())
    updated_at: Mapped[datetime] = mapped_column(default=func.utc_timestamp(), onupdate=func.utc_timestamp())

    category = relationship('CategoryEntity', back_populates='articles')
    tags = relationship('TagEntity', secondary=articles_tags, back_populates='articles')

    def to_json(self) -> dict[str, Any]:
        return {
            'title': self.title,
            'content': self.content,
            'publication_date': self.publication_date,
            'category_id': self.category_id,
        }


class CategoryEntity(Base):

    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    name: Mapped[str] = mapped_column(String(), nullable=True)
    description: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(default=func.utc_timestamp())
    updated_at: Mapped[datetime] = mapped_column(default=func.utc_timestamp(), onupdate=func.utc_timestamp())
    articles: Mapped[list[ArticleEntity]] = relationship('ArticleEntity', back_populates='category', lazy=False)

    def to_json(self) -> dict[str, Any]:
        return {
            'name': self.name,
            'description': self.description,
        }


class TagEntity(Base):

    __tablename__ = 'tags'

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    name: Mapped[str] = mapped_column(String(), nullable=True)
    created_at: Mapped[datetime] = mapped_column(default=func.utc_timestamp())

    articles = relationship('ArticleEntity', secondary=articles_tags, back_populates='tags')

    def to_json(self) -> dict[str, Any]:
        return {
            'name': self.name
        }
