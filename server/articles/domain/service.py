from application.ports.input import ArticleInputPort
from application.ports.output import ArticleOutputPort
from domain.model import Article
from dataclasses import dataclass


# todo (4):
"""
    Zakładam, że serwis domenowy ma za zadanie w ramach metod z input portów wywołać wszystkie odpowiadające
    side effect'y, czyli:
    
    port wejściowy create_product(), wywoła:
        1. dodanie artykułu do bazy (adapter db), 
        2. wysłanie danych broker'em do innego serwisu (adapter broker?)
        
    Nie mam jeszcze zaimplementowanego broker'a do przesłania tego, ale zastanawiam się już, bo możliwe, że 
    nie zrozumiałem tego do końca, jak ma się do tego 'event'. Czy nie mogę po prostu zrobić manager'a w ramach brokera
    który będzię implementacją output porta, i po prostu infectować go tutaj (identycznie jak repo)?
    
    Czy potrzebowałbym tutaj nadal czegoś więcej / czy coś pominąłem?
"""


@dataclass
class ArticleService(ArticleInputPort):
    article_output_port: ArticleOutputPort

    def create_article(self, article: Article) -> Article:
        return self.article_output_port.save_article(article)

    def update_article(self, article: Article) -> Article:
        ...

    def delete_article(self, id_: int) -> int:
        return self.article_output_port.delete_article(id_)

    def get_article_by_id(self, id_: int) -> Article | None:
        return self.article_output_port.get_article_by_id(id_)

    def get_article_by_title(self, title: str) -> Article | None:
        return self.article_output_port.get_article_by_title(title)
