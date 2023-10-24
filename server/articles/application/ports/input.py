from domain.model import Article
from abc import ABC, abstractmethod


class ArticleInputPort(ABC):

    @abstractmethod
    def create_article(self, article: Article) -> Article:
        pass

    @abstractmethod
    def update_article(self, article: Article) -> Article:
        pass

    @abstractmethod
    def delete_article(self, id_: int) -> int:
        pass

    @abstractmethod
    def get_article_by_id(self, id_: int) -> Article | None:
        pass

    @abstractmethod
    def get_article_by_title(self, title: str) -> Article | None:
        pass
