import sqlite3
from datetime import  datetime
from config import  database_name
from xlsxwriter.workbook import Workbook

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

    def export_to_excel(self):
        workbook = Workbook('inf.xlsx')
        worksheet = workbook.add_worksheet()
        with self.connection:
            ms =self.cursor.execute('SELECT * FROM active_user')
            for i,row in enumerate(ms):
                for j,value in enumerate(row):
                    worksheet.write(i+1,j,row[j])
        worksheet.write(0, 0, 'id')
        worksheet.write(0, 1, 'Chat_id')
        worksheet.write(0, 2, 'Время запроса')
        workbook.close()


a = SQLighter()
a.export_to_excel()