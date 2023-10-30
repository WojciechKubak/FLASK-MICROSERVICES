from application.ports.input import ArticleInputPort, CategoryInputPort
from domain.model import Article, Category
from dataclasses import dataclass
from typing import Any


@dataclass
class ArticleService:
    domain_service: ArticleInputPort

    def add_article(self, data: dict[str, Any]) -> Article:
        article_title = data.get('title')
        if self.domain_service.get_article_by_title(article_title):
            raise ValueError(f"Article '{article_title}' already exists")
        return self.domain_service.create_article(Article.from_json(data))

    def update_article(self, data: dict[str, Any]) -> Article:
        article_id = data.get('id')
        if not self.domain_service.get_article_by_id(article_id):
            raise ValueError(f"No article with id: {article_id}")
        return self.domain_service.update_article(Article.from_json(data))

    def delete_article(self, id_: int) -> int:
        if not self.domain_service.get_article_by_id(id_):
            raise ValueError(f"No article with id: {id_}")
        return self.domain_service.delete_article(id_)

    def get_article_by_id(self, id_: int) -> Article:
        if not (article := self.domain_service.get_article_by_id(id_)):
            raise ValueError(f"No article with id: {id_}")
        return article


@dataclass
class CategoryService:
    domain_service: CategoryInputPort

    def add_category(self, data: dict[str, Any]) -> Category:
        category_name = data.get('name')
        if self.domain_service.get_category_by_name(category_name):
            raise ValueError(f"Category '{category_name}' already exists")
        return self.domain_service.create_category(Category.from_json(data))

    def update_category(self, data: dict[str, Any]) -> Category:
        category_id = data.get('id')
        if not self.domain_service.get_category_by_id(category_id):
            raise ValueError(f"No category with id: {category_id}")
        return self.domain_service.update_category(Category.from_json(data))

    def delete_category(self, id_: int) -> int:
        if not self.domain_service.get_category_by_id(id_):
            raise ValueError(f"No category with id: {id_}")
        return self.domain_service.delete_category(id_)

    def get_category_by_id(self, id_: int) -> Category:
        if not (category := self.domain_service.get_category_by_id(id_)):
            raise ValueError(f"No category with id: {id_}")
        return category
