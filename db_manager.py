import sqlite3

conn = sqlite3.Connection('banking.db')
cur = conn.cursor()

def createtables ():
    
    cur.execute("""
                CREATE TABLE IF NOT EXISTS Words (
                    
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Word text NOT NULL,
                    
                    )""")
    conn.commit()




def InsertWords (words):
    for word in words:
        cur.execute("INSERT INTO Words (Word) VALUES (?)" ,(word))
        conn.commit()

    return cur.lastrowid

def DeleteDB():
    cur.execute("DROP TABLE IF EXISTS Words")
    conn.commit()












































