# vulnerable_login.py
import sqlite3

def login(username, password):
    conn = sqlite3.connect('users_vuln.db')
    cursor = conn.cursor()
    # VULNERABLE to SQL injection
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    return result is not None

if __name__ == '__main__':
    user = input("Username: ")
    pwd = input("Password: ")
    if login(user, pwd):
        print("Login successful")
    else:
        print("Invalid credentials")
