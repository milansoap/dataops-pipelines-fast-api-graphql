from pymongo import MongoClient
from mongo.config import mongo_conn_settings

class MongoConnection:
    """
    MongoDB database connection.
    """

    def __init__(self, settings: mongo_conn_settings) -> None:
        self.conn_string = f'mongodb://{settings.host}:{settings.port}/'
        self.client = MongoClient(self.conn_string)

    def connect(self) -> None:
        try:
            # The ismaster command is cheap and does not require auth.
            self.client.admin.command('ismaster')
            print("Successfully connected to MongoDB!")
        except Exception as e:
            print(f"Could not connect to MongoDB: {e}")

    def get_db(self, database_name: str = "mydatabase"):  # Default database name
        db = self.client[database_name]
        return db

    def close(self):
        self.client.close()
        print("MongoDB connection closed.")


if __name__ == "__main__":
    mongo_conn = MongoConnection(mongo_conn_settings)

    print(mongo_conn_settings)

    print("--- Testing connect() method ---")
    mongo_conn.connect()

    print("\n--- Testing get_db() method ---")
    db = mongo_conn.get_db("mydatabase")  # Specify the database name
    print(f"Connected to database: {db.name}")

    mongo_conn.close()