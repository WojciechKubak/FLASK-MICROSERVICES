from abc import ABC, abstractmethod
from typing import Optional


class ArticleInputPort(ABC):
    @abstractmethod
    def get_article(self, article_id: int) -> Optional[dict]:
        pass

    @abstractmethod
    def create_article(self, article_data: dict) -> dict:
        pass

    @abstractmethod
    def update_article(self, article_id: int, article_data: dict) -> Optional[dict]:
        pass

    @abstractmethod
    def delete_article(self, article_id: int) -> None:
        pass
