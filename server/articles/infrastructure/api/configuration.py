from domain.configuration import domain_article_service
from infrastructure.api.service import ArticleService

article_service = ArticleService(domain_article_service)
