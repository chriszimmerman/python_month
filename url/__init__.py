import sqlite3
conn = sqlite3.connect('example.db')

c = conn.cursor()

#c.execute("INSERT INTO urls VALUES (NULL, 'http://www.google.com')")

#conn.commit()

conn.close()
