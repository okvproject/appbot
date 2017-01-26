import sqlite3
from datetime import  datetime
from config import  database_name


class SQLighter:
    def __init__(self):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def insert_inf(self,message):
        with self.connection:
            insert_string = 'INSERT INTO active_user(id,chat_id, dateT) VALUES(NULL,"{}", "{}")'.format(str(message.chat.id),str(datetime.now()))
            self.cursor.execute(insert_string)
            self.connection.commit()

    def close(self):
        self.connection.close()


