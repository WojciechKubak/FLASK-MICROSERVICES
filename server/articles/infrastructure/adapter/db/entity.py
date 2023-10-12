from sqlalchemy import Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from typing import Any

Base = declarative_base()


class Article(Base):

    __tablename__ = 'articles'

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    title: Mapped[str] = mapped_column(String(), nullable=True)
    content: Mapped[str] = mapped_column(String(10000))
    publication_date: Mapped[datetime] = mapped_column(DateTime)
    category_id: Mapped[int] = mapped_column(Integer(), ForeignKey('categories.id'))
    created_at: Mapped[datetime] = mapped_column(default=func.utc_timestamp())
    updated_at: Mapped[datetime] = mapped_column(default=func.utc_timestamp(), onupdate=func.utc_timestamp())

    category = relationship('Category', back_populates='articles')

    def to_json(self) -> dict[str, Any]:
        return {
            'title': self.title,
            'content': self.content,
            'publication_date': self.publication_date,
            'category_id': self.category_id,
        }


class Category(Base):

    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    name: Mapped[str] = mapped_column(String(), nullable=True)
    description: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(default=func.utc_timestamp())
    updated_at: Mapped[datetime] = mapped_column(default=func.utc_timestamp(), onupdate=func.utc_timestamp())

    def to_json(self) -> dict[str, Any]:
        return {
            'name': self.name,
            'description': self.description,
        }


class Tag(Base):

    __tablename__ = 'tags'

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    name: Mapped[str] = mapped_column(String(), nullable=True)
    created_at: Mapped[datetime] = mapped_column(default=func.utc_timestamp())

    def to_json(self) -> dict[str, Any]:
        return {
            'name': self.name
        }


class ArticleTag(Base):

    __tablename__ = 'article_tags'

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    article_id: Mapped[int] = mapped_column(Integer(), ForeignKey('articles.id'))
    tag_id: Mapped[int] = mapped_column(Integer(), ForeignKey('tags.id'))
    created_at: Mapped[datetime] = mapped_column(default=func.utc_timestamp())

    article = relationship('Article', back_populates='article_tags')
    tag = relationship('Tag', back_populates='article_tags')

    def to_json(self) -> dict[str, Any]:
        return {
            'article_id': self.article_id,
            'tag_id': self.tag_id
        }
