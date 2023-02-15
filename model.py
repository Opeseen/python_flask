import sqlite3;

def show_color(username):
    connection = sqlite3.connect('flask_db.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(f"SELECT favorite_color FROM users WHERE username = '{username}' ORDER BY ID DESC;")
    color = cursor.fetchone()[0]

    connection.commit()
    cursor.close()
    connection.close()
    message = f"{username} Favorite color is {color}."
    return message


def check_passwd(username):
    connection = sqlite3.connect('flask_db.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(f"SELECT password FROM users WHERE username = '{username}' ORDER BY ID DESC")
    password = cursor.fetchone()

    if password is None:
        cursor.close()
        connection.close()
        return 'Wrong Password'
    else:
        cursor.close()
        connection.close()
        return ''.join(password)
   

def signup(username,password, favorite_color):
    connection = sqlite3.connect('flask_db.db',check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(f"SELECT username FROM users WHERE username = '{username}' ORDER BY ID DESC;")
    result = cursor.fetchone()

    if result is None:
        cursor.execute(f"INSERT INTO users(username,password,favorite_color) VALUES('{username}','{password}','{favorite_color}')")
        connection.commit()
        cursor.close()
        connection.close()
        
        return (f"User {username} have been successfully SignUP...")
    else:
        return (f"User {username} Already Exist!!!")
 