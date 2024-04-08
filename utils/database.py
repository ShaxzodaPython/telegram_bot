import psycopg2 as db
from main import config
import random

class Database:
    def __init__(self):
        self.conn = db.connect(
            database=config.DB_NAME,
            password=config.DB_PASS,
            user=config.DB_USER,
            host=config.DB_HOST,
            port=config.DB_PORT,
        )
        self.cursor = self.conn.cursor()

    def create_tables(self):
        user_table = """CREATE TABLE IF NOT EXISTS users(
        user_id SERIAL PRIMARY KEY,
        chat_id BIGINT NOT NULL,
        full_name VARCHAR(55),
        phone_number VARCHAR(15),
        location VARCHAR(55))"""

        photos_table = """CREATE TABLE IF NOT EXISTS photos(
        photo_id SERIAL PRIMARY KEY,
        user_id INT REFERENCES users(user_id),
        photo_id VARCHAR(250),
        status BOOLEAN DEFAULT false)"""

        likes_table = """
        CREATE TABLE IF NOT EXISTS likes(
        likes_id INT PRIMARY KEY,
        user_id INT REFERENCES users(users_id),
        photo_id INT REFERENCES photos(photo_id),
        is_like BOOLEAN DEFAULT false)"""

        self.cursor.execute(user_table)
        self.cursor.execute(photos_table)
        self.cursor.execute(likes_table)

        self.conn.commit()

    def get_user_by_chat_id(self, chat_id):
        query = f"SELECT * FROM users WHERE chat_id = {chat_id} AND status = true"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result


    def get_user_photo_by_chat_id(self, chat_id):
        query = f"SELECT * FROM users WHERE chat_id = {chat_id}"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result

    def add_user(self, data:dict):
        chat_id = data["chat_id"]
        full_name = data["full_name"]
        phone_number = data["phone_number"]
        location = data["location"]
        query = (f"""INSERT INTO users(chat_id, fullname, phone_number, location) 
                 VALUES ('{chat_id}', '{full_name}', '{phone_number}', '{location}')""")
        self.cursor.execute(query)
        self.conn.commit()
        return True

    def add_photto(self, data: dict):
        chat_id = data["chat_id"]
        photo_id = data["photo_id"]
        query = (f"""INSERT INTO photos(chat_id, photo_id, status) 
                 VALUES ('{chat_id}', '{photo_id}', true)""")
        self.cursor.execute(query)
        self.conn.commit()
        return True






        
        

