#!/usr/bin/env python

import psycopg2
import datetime

DB_NAME = "news"

conn = psycopg2.connect(database=DB_NAME)
cursor = conn.cursor()
cursor.execute("""select title, count(*) as num from articles cross join log
    where log.path like '/article/' || articles.slug group by articles.title
    order by num desc limit 3""")

rows = cursor.fetchall()

print "\n", "Question No, 1", "\n"

for row in rows:
    print row[0], " -- ", row[1], "views"

cursor.execute("""select author, count(*) as num from articles cross join log
    where log.path like '/article/' || articles.slug group by articles.author
    order by num desc""")
rows1 = cursor.fetchall()

cursor.execute("""select distinct authors.id,name from authors, articles where
    authors.id = articles.author order by id asc""")
rows2 = cursor.fetchall()

print "\n", "Question No, 2", "\n"

for row1 in rows1:
    for row2 in rows2:
        if row1[0] == row2[0]:
            print row2[1], " -- ", row1[1], " views "

cursor.execute("select * from dates")
rows3 = cursor.fetchall()

cursor.execute("""select waqt,count(*) from log cross join dates where status =
    '404 NOT FOUND' and date(time) = waqt group by waqt""")
rows4 = cursor.fetchall()

print "\n", "Question No, 3", "\n"

for row3 in rows3:
    for row4 in rows4:
        if row3[0] == row4[0] and ((row4[1] * 100.0) / row3[1]) > 1.0:
            x = datetime.datetime.strptime(row3[0].strftime('%Y-%m-%d'),
                                           '%Y-%m-%d')
            print x.strftime("%B %d, %Y"), " -- ",
            print (row4[1] * 100.0) / row3[1], "% errors "

conn.close()
