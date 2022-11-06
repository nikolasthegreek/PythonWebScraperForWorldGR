import sqlite3

conn = sqlite3.Connection('Words.db')
cur = conn.cursor()

def createtables ():
    
    cur.execute("""
                CREATE TABLE IF NOT EXISTS Words (
                    
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Word text NOT NULL
                    
                    )""")

    cur.execute("""
                CREATE TABLE IF NOT EXISTS Progres (
                    
                    Page INTEGER NOT NULL,
                    Let text NOT NULL
                    
                    )""")
    
    conn.commit()




def InsertWords (words):
    for word in words:
        cur.execute("INSERT INTO Words (Word) VALUES ('!')".replace("!",word))
        conn.commit()
    return cur.lastrowid

def SaveProses (Letter,Page):
    cur.execute('INSERT INTO Progres (Page,Let) VALUES (?,?)',(Page,Letter))
    conn.commit()
    return cur.lastrowid


def DeleteDB():
    cur.execute("DROP TABLE IF EXISTS Words")
    conn.commit()

if __name__ == "__main__":
    DeleteDB()
    createtables()
    
    conn.commit()


