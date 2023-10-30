from sqlalchemy import Integer, String, DateTime, ForeignKey, func, Table, Column
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

Base = declarative_base()


articles_tags = Table(
    'articles_tags',
    Base.metadata,
    Column('id', Integer(), primary_key=True),
    Column('article_id', Integer(), ForeignKey('articles.id'), primary_key=True),
    Column('tag_id', Integer(), ForeignKey('tags.id'), primary_key=True),
)


class CategoryEntity(Base):

    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    name: Mapped[str] = mapped_column(String(), nullable=True)
    description: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(default=func.utc_timestamp())
    updated_at: Mapped[datetime] = mapped_column(default=func.utc_timestamp(), onupdate=func.utc_timestamp())

    articles = relationship('ArticleEntity', back_populates='category', lazy='joined')


class TagEntity(Base):

    __tablename__ = 'tags'

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    name: Mapped[str] = mapped_column(String(), nullable=True)
    created_at: Mapped[datetime] = mapped_column(default=func.utc_timestamp())

    articles = relationship('ArticleEntity', secondary=articles_tags, back_populates='tags', lazy='joined')


class ArticleEntity(Base):

    __tablename__ = 'articles'

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    title: Mapped[str] = mapped_column(String())
    content: Mapped[str] = mapped_column(String(10000), nullable=True)
    publication_date: Mapped[datetime] = mapped_column(DateTime)
    category_id: Mapped[int] = mapped_column(Integer(), ForeignKey('categories.id'))
    created_at: Mapped[datetime] = mapped_column(default=func.utc_timestamp())
    updated_at: Mapped[datetime] = mapped_column(default=func.utc_timestamp(), onupdate=func.utc_timestamp())

    category: Mapped[CategoryEntity] = relationship(CategoryEntity, back_populates='articles')
    tags: Mapped[list[TagEntity]] = relationship(
        TagEntity, secondary=articles_tags, back_populates='articles')
