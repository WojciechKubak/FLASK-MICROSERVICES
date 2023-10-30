from infrastructure.db.entity import ArticleEntity, CategoryEntity, TagEntity
from dataclasses import dataclass, field
from datetime import datetime
from typing import Self, Any, Optional


@dataclass
class Article:
    id_: int | None
    title: str
    content: str
    publication_date: datetime
    category_id: int
    tags: list[int] = field(default_factory=list)

    def to_entity(self) -> ArticleEntity:
        entity_data = {
            'title': self.title,
            'content': self.content,
            'publication_date': self.publication_date,
            'category_id': self.category_id
        }
        return ArticleEntity(**entity_data | {'id': self.id_} if self.id_ else entity_data)

    def to_json(self) -> dict[str, Any]:
        return {
            'id': self.id_,
            'title': self.title,
            'content': self.content,
            'publication_date': self.publication_date,
            'category_id': self.category_id,
            'tags': self.tags
        }

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> Self:
        return cls(**data | {'id_': data.pop('id')})

    @classmethod
    def from_entity(cls, article: ArticleEntity) -> Self:
        return cls(
            id_=article.id,
            title=article.title,
            content=article.content,
            publication_date=article.publication_date,
            category_id=article.category_id,
            tags=[tag.id for tag in article.tags] if 'tags' in article.__dict__ else []
        )


@dataclass
class Category:
    id_: int | None
    name: str
    description: str

    def to_entity(self) -> CategoryEntity:
        entity_data = {
            'id': self.id_,
            'name': self.name,
            'description': self.description
        }
        return CategoryEntity(**entity_data | {'id': self.id_} if self.id_ else entity_data)

    def to_json(self) -> dict[str, Any]:
        return {
            'id': self.id_,
            'name': self.name,
            'description': self.description,
        }

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> Self:
        return cls(**data | {'id_': data.pop('id')})

    @classmethod
    def from_entity(cls, category: CategoryEntity) -> Self:
        return cls(
            id_=category.id,
            name=category.name,
            description=category.description,
        )


@dataclass(frozen=True)
class Tag:
    id_: Optional[int] = None
    name: Optional[str] = None

    def to_entity(self) -> TagEntity:
        entity_data = {
            'name': self.name
        }
        return TagEntity(**entity_data | {'id': self.id_} if self.id_ else entity_data)

    def to_json(self) -> dict[str, Any]:
        return {
            'id': self.id_,
            'name': self.name,
        }

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> Self:
        return cls(
            id_=data.get('id'),
            name=data.get('name'),
        )

    @classmethod
    def from_entity(cls, tag: TagEntity) -> Self:
        return cls(
            id_=tag.id,
            name=tag.name,
            articles=[Article.from_entity(article) for article in tag.articles]
        )
