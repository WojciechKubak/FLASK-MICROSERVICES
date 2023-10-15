from ..application.ports.input import ArticleInputPort


class ArticleService(ArticleInputPort):

    def get_article(self, article_id: int) -> Optional[dict]:
        pass

    def create_article(self, article_data: dict) -> dict:
        pass

    def update_article(self, article_id: int, article_data: dict) -> Optional[dict]:
        pass

    def delete_article(self, article_id: int) -> None:
        pass
