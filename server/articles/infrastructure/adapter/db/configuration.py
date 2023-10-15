from entity import Category, Article, Tag, ArticleTag
from connection import MySQLConnectionStringBuilder
from repository import CrudRepository
from sqlalchemy import create_engine


connection_string = MySQLConnectionStringBuilder.builder().build()
engine = create_engine(connection_string)

category_repository = CrudRepository(engine, Category)
article_repository = CrudRepository(engine, Article)
tag_repository = CrudRepository(engine, Tag)
article_tag_repository = CrudRepository(engine, ArticleTag)
