This source code solves the three following questions based on the news database-
    1. What are the most popular three articles of all time?
    2. Who are the most popular article authors of all time?
    3. On which days did more than 1% of requests lead to errors?

I have created following view for this purpose-
    create view dates as select date(time) as waqt, count(*) from log group by waqt;

    View "public.dates"
 Column |  Type  | Modifiers
--------+--------+-----------
 waqt   | date   |
 count  | bigint |

Prerequisite-
    1.  Python installed on the system.
    2.  "news" postgresql database server should be up with the "dates" view created in it.

Steps to run-
    1.  Run following command - python LogAnalysis.py
