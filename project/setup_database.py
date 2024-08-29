import sqlite3

# Setup database
conn = sqlite3.connect('internship.db')
c = conn.cursor()

c.execute('''
CREATE TABLE internships (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company TEXT NOT NULL,
    position TEXT NOT NULL,
    city TEXT NOT NULL
)
''')

conn.commit()
conn.close()

print("Database setup complete!")
