from abc import ABC, abstractmethod


class ArticleOutputPort(ABC):

    @abstractmethod
    def save_article(self, product) -> None:
        pass

    @abstractmethod
    def send_article(self, article) -> None:
        pass

    @abstractmethod
    def send_message(self, article) -> None:
        pass
