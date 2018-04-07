import sqlite3

getnews = sqlite3.connect('GetNews.sqlite')
create_table = 'create table getnews (time varchar(50),title varchar(512),url varchar(512))'
getnews.execute(create_table)
