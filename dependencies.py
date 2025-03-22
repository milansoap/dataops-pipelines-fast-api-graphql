# app/dependencies.py
from config import conn_settings
from db import PostgresConnection

def get_db():
    connection = PostgresConnection(conn_settings)
    db = connection.SessionLocal()
    try:
        yield db
    finally:
        db.close()

from services.player import PlayerCRUD
player_crud_service = PlayerCRUD(db=next(get_db()))