from application.ports.input import ArticleInputPort
from domain.model import Article
from dataclasses import dataclass
from typing import Any


@dataclass
class ArticleService:
    article_domain_service: ArticleInputPort

    def add_article(self, data: dict[str, Any]) -> Article:
        article_title = data.get('title')
        if self.article_domain_service.get_article_by_title(article_title):
            raise ValueError(f"Article '{article_title}' already exists")
        return self.article_domain_service.create_article(Article.from_json(data))

    def update_article(self, id_: int, data: dict[str, Any]) -> Article:
        if not (article := self.article_domain_service.get_article_by_id(id_)):
            raise ValueError(f"No article with id: {id_}")
        return self.article_domain_service.update_article()

    def delete_article(self, id_: int) -> int:
        if not self.article_domain_service.get_article_by_id(id_):
            raise ValueError(f"No article with id: {id_}")
        return self.article_domain_service.delete_article(id_)

    def get_article_by_id(self, id_: int) -> Article:
        if not (article := self.article_domain_service.get_article_by_id(id_)):
            raise ValueError(f"No article with id: {id_}")
        return article
