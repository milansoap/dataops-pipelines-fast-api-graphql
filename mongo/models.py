# app/models.py
from mongoengine import Document, IntField, ListField, connect
from mongo.config import mongo_conn_settings

# Initialize the connection
connect(db="football_db", host=mongo_conn_settings.host, port=mongo_conn_settings.port)

class Matches(Document):
    match_id = IntField()
    team_home = IntField()
    team_away = IntField()
    events = ListField()

    meta = {'collection': 'matches'} # Specify the collection name