from abc import ABC, abstractmethod


class ArticleCreationUseCase(ABC):

    @abstractmethod
    def create_article(self, article) -> None:
        pass
