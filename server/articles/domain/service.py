from application.ports.input import ArticleInputPort, CategoryInputPort
from application.ports.output import ArticleOutputPort, CategoryOutputPort
from domain.model import Article, Category
from dataclasses import dataclass


@dataclass
class ArticleService(ArticleInputPort):
    article_output_port: ArticleOutputPort

    def create_article(self, article: Article) -> Article:
        added_article = self.article_output_port.save_article(article)
        return added_article

    def update_article(self, article: Article) -> Article:
        updated_article = self.article_output_port.update_article(article)
        return updated_article

    def delete_article(self, id_: int) -> int:
        return self.article_output_port.delete_article(id_)

    def get_article_by_id(self, id_: int) -> Article | None:
        return self.article_output_port.get_article_by_id(id_)

    def get_article_by_title(self, title: str) -> Article | None:
        return self.article_output_port.get_article_by_title(title)


@dataclass
class CategoryService(CategoryInputPort):
    category_output_port: CategoryOutputPort

    def create_category(self, category: Category) -> Category:
        added_category = self.category_output_port.save_category(category)
        return added_category

    def update_category(self, category: Category) -> Category:
        updated_category = self.category_output_port.update_category(category)
        return updated_category

    def delete_category(self, id_: int) -> int:
        return self.category_output_port.delete_category(id_)

    def get_category_by_id(self, id_: int) -> Category | None:
        return self.category_output_port.get_category_by_id(id_)

    def get_category_by_name(self, name: str) -> Category | None:
        return self.category_output_port.get_category_by_name(name)
