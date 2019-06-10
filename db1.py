import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def CreateTable():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value TEXT)')
##def data_entry():
##    c.execute("INSERT INTO stuffToPlot VALUES(145345345,'2016-010-01', 'PYTHON', 8)")
##    conn.commit()
##    conn.close()

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,10)
    c.execute("INSERT INTO stuffToPlot(unix, datestamp, keyword, value) VALUES(?, ?, ?, ?)",
              (unix,date,keyword,value))
    conn.commit()

CreateTable()
for i in range(10):
    dynamic_data_entry()
    time.sleep(1)
c.close()
conn.close()
















##data_entry()
