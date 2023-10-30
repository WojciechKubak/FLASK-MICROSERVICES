from domain.configuration import domain_article_service, domain_category_service
from infrastructure.api.service import ArticleService, CategoryService

article_service = ArticleService(domain_article_service)
category_service = CategoryService(domain_category_service)
