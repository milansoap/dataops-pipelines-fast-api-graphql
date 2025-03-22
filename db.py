from dataclasses import dataclass
from sqlalchemy import create_engine, text, inspect
from sqlalchemy.orm import sessionmaker


@dataclass(frozen=True)
class ConnectionSettings:
    """Connection Settings."""
    host: str
    database: str
    username: str
    password: str
    port: str = '5432'


class PostgresConnection:
    """
    PostgresSQL database connection.
    """

    def __init__(self, conn_settings: ConnectionSettings, echo: bool = False) -> None:
        self.conn_string = f'postgresql://{conn_settings.username}:{conn_settings.password}@{conn_settings.host}:{conn_settings.port}/{conn_settings.database}'
        self.engine = create_engine(self.conn_string, echo=echo)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def connect(self) -> None:
        """Estimate connection."""
        self.conn = self.engine.connect()

    def get_db(self):
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()