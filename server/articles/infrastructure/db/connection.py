from dataclasses import dataclass, field
from typing import Self, Any


@dataclass
class MySQLConnectionStringBuilder:
    _config: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        if not self._config:
            self._config = {
                'host': 'localhost',
                'database': 'db_1',
                'user': 'user',
                'password': 'user1234',
                'port': 3307
            }

    def host(self, new_host: str) -> Self:
        self._config['host'] = new_host
        return self

    def user(self, new_user: str) -> Self:
        self._config['user'] = new_user
        return self

    def password(self, new_password: str) -> Self:
        self._config['password'] = new_password
        return self

    def database(self, new_database: str) -> Self:
        self._config['database'] = new_database
        return self

    def port(self, new_port: int) -> Self:
        self._config['port'] = new_port
        return self

    def build(self) -> str:
        return f"mysql://{self._config['user']}:{self._config['password']}@" \
               f"{self._config['host']}:{self._config['port']}/{self._config['database']}"

    @classmethod
    def builder(cls) -> Self:
        return cls()
