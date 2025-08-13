# create_vuln_db.py
import sqlite3

conn = sqlite3.connect('users_vuln.db')
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
''')
try:
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('admin', 'password123'))
except sqlite3.IntegrityError:
    pass
conn.commit()
conn.close()
print("Created users_vuln.db with sample user: admin / password123")
