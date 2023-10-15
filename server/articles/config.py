from dataclasses import dataclass
from typing import ClassVar
import os


@dataclass
class BaseConfig:
    TESTING: ClassVar[bool] = True
    SQLALCHEMY_DATABASE_URI: ClassVar[str] = 'mysql://user:user1234@mysql:3307/db_1'


@dataclass
class ProductionConfig(BaseConfig):
    TESTING: ClassVar[bool] = False
    SQLALCHEMY_TRACK_MODIFICATIONS: ClassVar[bool] = True
    SQLALCHEMY_DATABASE_URI: ClassVar[str] = os.environ.get('DATABASE_URI')


@dataclass
class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_TRACK_MODIFICATIONS: ClassVar[bool] = False


@dataclass
class TestingConfig(BaseConfig):
    SQLALCHEMY_TRACK_MODIFICATIONS: ClassVar[bool] = False
    SQLALCHEMY_DATABASE_URI: ClassVar[str] = 'mysql://user:user1234@localhost:3308/db_test'
