# create_secure_db.py
import sqlite3
import bcrypt

conn = sqlite3.connect('users_secure.db')
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password_hash TEXT
)
''')
password = 'password123'
hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
try:
    c.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", ('admin', hashed))
except sqlite3.IntegrityError:
    pass
conn.commit()
conn.close()
print("Created users_secure.db with sample user: admin / password123 (hashed)")
