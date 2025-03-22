from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from postgres.config import conn_settings
from urllib.parse import quote_plus


class PostgresConnection:
    """
    PostgresSQL database connection.
    """

    def __init__(self, settings: conn_settings, echo: bool = False) -> None:
        # Encode username and password
        user = quote_plus(settings.user)
        password = quote_plus(settings.password)
        self.conn_string = f'postgresql://{user}:{password}@{settings.host}:{settings.port}/{settings.database}'
        self.engine = create_engine(self.conn_string, echo=echo, pool_size=50)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def connect(self) -> None:
        self.conn = self.engine.connect()
        self.conn.close()


    def get_db(self):
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()


if __name__ == "__main__":

    postgres_conn = PostgresConnection(conn_settings)

    print(conn_settings)

    print("--- Testing connect() method ---")
    postgres_conn.connect()

    print("\n--- Testing get_db() method ---")
    db_generator = postgres_conn.get_db()
    try:
        db = next(db_generator)
    except StopIteration:
        pass
    except Exception:
        pass