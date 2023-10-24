from application.ports.output import ArticleOutputPort
from infrastructure.db.repository import ArticleRepository
from domain.model import Article
from dataclasses import dataclass


# todo (2):
"""
    Warstwa poniżej odpowiada za konwersję modeli domenowych do modeli bazodanowych (Entity), wymaga on poprawy, 
    ale wyjściowo zakładam, że:
    
        1. model domenowy jest konwertowany na model bazodanowy, 
        2. przy konwersji nadawany jest ID,
        3. następuje zapis do bazy
    
    Po tym procesie, prawdopodobnie chciałbym odzyskać dane z Entity z powrotem do modelu domenowego, 
    żeby móc przekazać go razem z id dla użytkownika (po wykonaniu czegoś w stylu to_json())?
    
    Jeżeli te założenie jest prawdziwe do model domenowy musi:
    
        1. przekonwertować surowe dane z Route'a (dict'a) na model domenowy, 
        2. przekonwertować model domenowy na model bazodanowy (entity), 
        3. przekonwertować model bazodanowy z powrotem na model domenowy (tym razem już z zawartym id po dodaniu do bazy), 
        4. przekonwertować model domenowy na serializowalny format (przy odpowiedzi dla client'a)
    
    Czy nie jest tego za dużo? to potencjalne 4 metody w ramach modelu domenowego do zaimplementowania.
    prosiłbym o nakierowanie, bo pewnie czegoś nie rozumiem.
"""

# todo (3):
"""
    Zakładam, że przy utworzeniu rekordu dla client'a powinienem zwrócić json'a z nowo utworzonym obiektem, 
    dla delete powinno być to coś w stylu samego id. No i tutaj pytanie, która warstwa powinna zwracać taki obiekt? 
    W mojej implementacji repozytorium CRUD (articles/infrastructure/db/repository) metody są wyjściowo voidowe, 
    więc realnie zwracam te dane w ramach poniższych metod, ale czy tak to powinno wyglądać? Może w jakiejś 
    innej warstwie?
"""


@dataclass
class ArticleOutputPortAdapter(ArticleOutputPort):
    article_repository: ArticleRepository

    def save_article(self, article: Article) -> Article:
        self.article_repository.add(article.to_entity())
        return article

    def update_article(self, article: Article) -> Article:
        self.article_repository.update()
        return article

    def delete_article(self, id_: int) -> int:
        self.article_repository.delete(id_)
        return id_

    def get_article_by_id(self, id_: int) -> Article | None:
        return self.article_repository.find_by_id(id_)

    def get_article_by_title(self, title: str) -> Article | None:
        return self.article_repository.find_by_title(title)
