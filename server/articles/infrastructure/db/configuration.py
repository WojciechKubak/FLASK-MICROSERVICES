from infrastructure.db.entity import CategoryEntity, ArticleEntity, TagEntity
from infrastructure.db.connection import MySQLConnectionStringBuilder
from infrastructure.db.repository import CrudRepository, ArticleRepository
from sqlalchemy import create_engine

connection_string = MySQLConnectionStringBuilder.builder().host('mysql').build()
engine = create_engine(connection_string)

article_repository = ArticleRepository(engine)
category_repository = CrudRepository(engine, CategoryEntity)
tag_repository = CrudRepository(engine, TagEntity)
