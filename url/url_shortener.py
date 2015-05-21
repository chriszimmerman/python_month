import sqlite3
conn = sqlite3.connect('example.db')

c = conn.cursor()

c.execute("INSERT INTO urls VALUES (NULL, 'http://www.google.com')")

conn.commit()

conn.close()

class URLShortener:
    def shorten_url(self, url):
        return 0; 

#create database
#take url and save in db
#get row id and convert id to string
#this string is the url shared
#when string is used as input, perform inverse function from string to row id
#get that row from the database
