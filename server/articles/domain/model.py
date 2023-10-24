from infrastructure.db.entity import ArticleEntity
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Self


@dataclass
class Category:
    name: str
    description: str


# todo (5):
"""
    Uświadomiłem sobie, że w ramach modeli domenowych będę jednak potrzebował id_, chciałbym je tutaj dodać, ale
    zastanawiam się, jak to zrobić, chodzi o to, że:
    
    musiałbym ustawić id_ jako: id_: int = field(default=None),
    
    no bo modele tworzone przykładowo w ramach add_article po samej konwersji z dict'a nie posiadają id, 
    przy takiej implementacji, jako, że pole id_ jest defaultowe to musi być ustawione w taki sposób:
    
    @dataclass
        class Article:
        title: str
        content: str
        publication_date: datetime
        category_id: int
        id_: int = field(default=None)
    
    co już samo w sobie wygląda dziwnie, 
    
    druga kwestia to konwersja, jeżeli obiekt z id_ = None przekonwertuję na model bazodanowy, to dostanę błąd (chyba), 
    z drugiej strony, jeżeli te id_ będzie, to raczej mam do czynienia z metodą put (nowe pola + istniejące id). 

    oczywiście można to obsłużyć w ramach metod to_entity(), ale wydaje mi się, że jest lepsze | łatwiejsze rozwiązanie
    którego nie za bardzo widzę
"""


@dataclass
class Article:
    id: int | None = None
    title: str
    content: str
    publication_date: datetime
    category_id: int

    def to_entity(self) -> ArticleEntity:
        return ArticleEntity(**self.__dict__)

    def to_json(self) -> dict[str, Any]:
        return self.__dict__

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> Self:
        return cls(**data)


@dataclass
class Tag:
    name: str


@dataclass
class ArticleTag:
    article_id: int
    tag_id: int
