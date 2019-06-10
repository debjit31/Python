import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
style.use("fivethirtyeight")

conn = sqlite3.connect('tutorial.db')#Connect to the database
c = conn.cursor()

def CreateTable():  #Create a Table
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value TEXT)')
    c.execute("INSERT INTO stuffToPlot VALUES(145345345,'2016-010-01', 'PYTHON', 8)")
    conn.commit()
    conn.close()

def dynamic_data_entry():   #Dynamic Entry In a Database
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,10)
    c.execute("INSERT INTO stuffToPlot(unix, datestamp, keyword, value) VALUES(?, ?, ?, ?)",
              (unix,date,keyword,value))
    conn.commit()


def read_from_db():#Extract data from database
        c.execute("SELECT keyword, unix  FROM stuffToPlot WHERE unix > 32156 ")
##        data = c.fetchall()
##        print(data)
        for row in c.fetchall():
            print(row)


def graph_data():
    c.execute('SELECT datestamp, value FROM stuffToPlot')
    dates = []
    values = []
    for row in c.fetchall():
        print(row[0])
        print(datetime.datetime.fromtimestamp(row[0]))
        #dates.append()











































              

##CreateTable()
##data_entry()
##for i in range(10):
##    dynamic_data_entry()
##    time.sleep(1)
##read_from_db()
        graph_data()
c.close()
conn.close()
















