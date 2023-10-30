from domain.model import Article, Category
from abc import ABC, abstractmethod


class ArticleOutputPort(ABC):

    @abstractmethod
    def save_article(self, article: Article) -> Article:
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


class ArticleEventPublisher(ABC):

    @abstractmethod
    def publish_product_created_event(self, event) -> None:
        pass


class CategoryOutputPort(ABC):

    @abstractmethod
    def save_category(self, category: Category) -> Category:
        pass

    @abstractmethod
    def update_category(self, category: Category) -> Category:
        pass

    @abstractmethod
    def delete_category(self, id_: int) -> int:
        pass

    @abstractmethod
    def get_category_by_id(self, id_: int) -> Category | None:
        pass

    @abstractmethod
    def get_category_by_name(self, name: str) -> Category | None:
        pass
