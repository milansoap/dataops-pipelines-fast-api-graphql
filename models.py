# app/models.py
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

from db import PostgresConnection, ConnectionSettings
from dependencies import conn_settings

# Initialize the connection
connection = PostgresConnection(conn_settings)

# Use the metadata from the connection
Base = declarative_base()

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    surname = Column(String, index=True)
    position = Column(String)
    origin = Column(String)
    height = Column(Float)
    weight = Column(Float)