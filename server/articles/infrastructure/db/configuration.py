from infrastructure.db.connection import MySQLConnectionStringBuilder
from infrastructure.db.repository import CrudRepository, ArticleRepository, CategoryRepository
from infrastructure.db.entity import TagEntity
from sqlalchemy import create_engine

connection_string = MySQLConnectionStringBuilder.builder().host('mysql').build()
engine = create_engine(connection_string)

article_repository = ArticleRepository(engine)
category_repository = CategoryRepository(engine)
tag_repository = CrudRepository(engine, TagEntity)
