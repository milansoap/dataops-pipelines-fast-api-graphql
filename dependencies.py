from postgres.config import conn_settings
from postgres.conn import PostgresConnection

def get_db():
    connection = PostgresConnection(conn_settings)
    db = connection.SessionLocal()
    try:
        yield db
    finally:
        db.close()

from services.players.players_queries import PlayerCRUD
player_crud_service = PlayerCRUD(db=next(get_db()))