import sqlite3
import PyQt5

con = sqlite3.connect('coffee.sqlite')
cur = con.cursor()

query = '''SELECT * FROM data'''

data = cur.execute(query).fetchall()
con.close()

for i in data:
    print(*i)