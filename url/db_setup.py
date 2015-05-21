import sqlite3
conn = sqlite3.connect('example.db')

c = conn.cursor()

c.execute('''CREATE TABLE urls 
             (id integer primary key autoincrement, url text)''')
conn.commit()

conn.close()
