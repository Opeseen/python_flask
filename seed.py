import sqlite3;

connection = sqlite3.connect('flask_db.db',check_same_thread=False)
cursor = connection.cursor()

cursor.execute('''INSERT INTO users(username,password,favorite_color) VALUES('Opeyemi','1234','Red')''')
cursor.execute('''INSERT INTO users(username,password,favorite_color) VALUES('Mike','1234','Blue')''')
cursor.execute('''INSERT INTO users(username,password,favorite_color) VALUES('Tony','1234','Yellow')''')


print("Data Inserted in the table: ")

data = cursor.execute('''SELECT * FROM users''')
for row in data:
  print(row)

connection.commit()
cursor.close()
connection.close()