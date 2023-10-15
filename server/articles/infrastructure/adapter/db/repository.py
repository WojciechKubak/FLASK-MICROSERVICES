from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import Engine
from dataclasses import dataclass
from functools import wraps
from typing import Callable, Any


@dataclass
class CrudRepository:
    _engine: Engine
    _entity: type[DeclarativeBase]

    def __post_init__(self):
        self._entity_type = type(self._entity)

        session_maker = self.create_session()
        self.session = session_maker()

    def create_session(self) -> sessionmaker:
        return sessionmaker(bind=self._engine, expire_on_commit=False)

    def session_scope(self):
        def decorator(method: Callable):
            @wraps(method)
            def wrapper(*args: tuple[Any], **kwargs: dict[str, Any]):
                try:
                    result = method(self, *args, **kwargs)
                    self.session.commit()
                    return result
                except Exception:
                    self.session.rollback()
                    raise
                finally:
                    self.session.close()

            return wrapper

        return decorator

    @session_scope
    def add(self, item: Any) -> None:
        self.session.add(item)

    @session_scope
    def update(self, item: Any) -> None:
        self.session.merge(item)

    @session_scope
    def delete(self, id_: int) -> None:
        item = self.session.query(self._entity_type).filter_by(id=id_).first()
        self.session.delete(item)

    @session_scope
    def find_by_id(self, id_: int) -> Any:
        return self.session.query(self._entity_type).filter_by(id=id_).first()
