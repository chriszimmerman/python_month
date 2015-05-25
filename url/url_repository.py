import sqlite3

class URLRepository:
    def get_row(self, id):
        connection = sqlite3.connect('example.db')
        cursor = connection.cursor()
        cursor.execute('SELECT url FROM urls WHERE id = ' + str(id) + ';');
        row = cursor.fetchone()
        connection.close()
        return row[0] 

    def insert_row(self, url):
        connection = sqlite3.connect('example.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO urls (url) VALUES (\'' + url + '\');');
        connection.commit();
        connection.close()
        return 
