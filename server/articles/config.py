from infrastructure.db.connection import MySQLConnectionStringBuilder
from dataclasses import dataclass
from typing import Type
import os


@dataclass
class BaseConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = MySQLConnectionStringBuilder.builder().host('mysql').build()


@dataclass
class ProductionConfig(BaseConfig):
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')


@dataclass
class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_TRACK_MODIFICATIONS = False


@dataclass
class TestingConfig(BaseConfig):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = MySQLConnectionStringBuilder.builder().database('db_test').port(3308).build()


def get_config() -> Type[BaseConfig]:
    return {
        'production': ProductionConfig,
        'development': DevelopmentConfig,
        'testing': TestingConfig
    }.get(os.environ.get('APP_CONFIG'), BaseConfig)
