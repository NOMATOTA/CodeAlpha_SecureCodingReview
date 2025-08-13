# secure_login.py
import sqlite3
import bcrypt

def login(username, password):
    conn = sqlite3.connect('users_secure.db')
    cursor = conn.cursor()
    cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()
    conn.close()
    if not row:
        return False
    stored_hash = row[0].encode('utf-8')
    return bcrypt.checkpw(password.encode('utf-8'), stored_hash)

if __name__ == '__main__':
    user = input("Username: ")
    pwd = input("Password: ")
    if login(user, pwd):
        print("Login successful")
    else:
        print("Invalid credentials")
