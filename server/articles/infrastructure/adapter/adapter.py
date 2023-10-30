from application.ports.output import ArticleOutputPort, CategoryOutputPort
from infrastructure.db.repository import ArticleRepository, CategoryRepository
from domain.model import Article, Category
from dataclasses import dataclass


@dataclass
class ArticleOutputPortAdapter(ArticleOutputPort):
    article_repository: ArticleRepository

    def save_article(self, article: Article) -> Article:
        article_to_add = article.to_entity()
        self.article_repository.add(article_to_add)
        return Article.from_entity(article_to_add)

    def update_article(self, article: Article) -> Article:
        article_to_update = article.to_entity()
        self.article_repository.update(article_to_update)
        return Article.from_entity(article_to_update)

    def delete_article(self, id_: int) -> None:
        self.article_repository.delete(id_)

    def get_article_by_id(self, id_: int) -> Article | None:
        if article := self.article_repository.find_by_id(id_):
            return Article.from_entity(article)
        return None

    def get_article_by_title(self, title: str) -> Article | None:
        if article := self.article_repository.find_by_title(title):
            return Article.from_entity(article)
        return None


@dataclass
class CategoryOutputPortAdapter(CategoryOutputPort):
    category_repository: CategoryRepository

    def save_category(self, category: Category) -> Category:
        category_to_add = category.to_entity()
        self.category_repository.add(category_to_add)
        return Category.from_entity(category_to_add)

    def update_category(self, category: Category) -> Category:
        category_to_update = category.to_entity()
        self.category_repository.update(category_to_update)
        return Category.from_entity(category_to_update)

    def delete_category(self, id_: int) -> None:
        self.category_repository.delete(id_)

    def get_category_by_id(self, id_: int) -> Category | None:
        if category := self.category_repository.find_by_id(id_):
            return Category.from_entity(category)
        return None

    def get_category_by_name(self, name: str) -> Category | None:
        if category := self.category_repository.find_by_name(name):
            return Category.from_entity(category)
        return None
