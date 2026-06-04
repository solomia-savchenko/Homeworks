import sqlite3
import random

conn = sqlite3.connect("app.db")

cursor = conn.cursor()

# cursor.execute("""
# create table if not exists genres (
# id integer primary key autoincrement,
# name varchar(50) not null unique,
# is_available boolean not null
# )
# """)

# conn.commit()

# cursor.execute("""
# insert into genres (name, is_available) values
# ('Thrillers', true),
# ('Drama', true),
# ('Science', true)
# """)

# conn.commit()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS books (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   name VARCHAR NOT NULL UNIQUE,
#   desc TEXT,
#   genre_id INTEGER NOT NULL,
#   FOREIGN KEY (genre_id) REFERENCES genres(id)
# );
# """)

# conn.close()

# cursor.execute("""
# insert into books (name, desc, genre_id) values
# ('book 1', 'supersecret!', 1),
# ('book 2', 'supersecret!', 2),
# ('book 3', 'supersecret!', 3)
# """)

# conn.commit()

# for i in range(4, 1000):
#   cursor.execute(f"""
#       insert into books (name, desc, genre_id) values
#       ('book {i}', 'supersecret!', {random.randint(1, 3)})
#   """)

#   conn.commit()

# cursor.execute("""
# select books.name, genres.name
# from books
# join genres on books.genre_id = genres.id
# where books.name like 'book 3'
# order by books.name desc
# limit 50
# """)

# rows = cursor.fetchall()

# for row in rows:
#   print(row)

# cursor.execute("""
# UPDATE books
# SET name = 'Hobbit', genre_id = 1
# WHERE id = 999
# """)

# cursor.execute("""
# ALTER TABLE books
# ADD COLUMN price double;
# """)

# conn.commit()

# cursor.execute("""
# UPDATE books
# SET price = 30
# WHERE id = 999
# """)

# conn.commit()

# cursor.execute("""
# select books.name, genres.name, books.price
# from books
# join genres on books.genre_id = genres.id
# where books.id = 999
# """)

# rows = cursor.fetchall()

# for row in rows:
#   print(row)


cursor.execute("""
DELETE FROM books
""")

conn.commit()

cursor.execute("""
select books.name, genres.name, books.price
from books
join genres on books.genre_id = genres.id
where books.id = 998
""")

rows = cursor.fetchall()

for row in rows:
    print(row)