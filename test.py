import sqlite3


connection=sqlite3.connect('data.db')
cursor=connection.cursor()

createTable="CREATE TABLE users(id int,username text,password text)"
cursor.execute(createTable)

users=[
    (1,'bob','asdf'),
    (2,'john','doe')
]
insertQuery="INSERT INTO users VALUES(?,?,?)"
cursor.executemany(insertQuery,users)

selectQuery="SELECT * FROM users"
for row in cursor.execute(selectQuery):
    print(row)
connection.commit()

connection.close()
