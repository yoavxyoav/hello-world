import sqlite3
import time
import datetime
import random

# connection. creates the file if it doesn't exist
conn = sqlite3.connect('tut.db')
c = conn.cursor()  # cursor. this is whats's doing the execution of things


def carate_table():
    c.execute(
        'CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')


def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(7654567, '2016-01-01', 'Python', 8)")
    conn.commit()  # saving


def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(
        unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0, 10)
    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)", (
        unix, date, keyword, value))
    conn.commit()


def read_from_db():
    c.execute("SELECT * FROM stuffToPlot")  # the cursor is now populated
    # data = c.fetchall()  # getting everything at the cursor
    # print(data)
    for row in c.fetchall():
        print(row)


# carate_table()
# data_entry()

# for i in range(10):
#     dynamic_data_entry()
#     time.sleep(1)
read_from_db()
c.close()
conn.commit()
