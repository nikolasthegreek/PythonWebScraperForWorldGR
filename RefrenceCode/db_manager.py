
import sqlite3

conn = sqlite3.Connection('banking.db')
cur = conn.cursor()

def createtables ():
    
    cur.execute("""
                CREATE TABLE IF NOT EXISTS CUSTOMERS (
                    
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name text NOT NULL,
                    surname text NOT NULL,
                    dateofbirth text NOT NULL
                    
                    )""")
    conn.commit()
                
    cur.execute("""
                CREATE TABLE IF NOT EXISTS ACCOUNTS (
                    
                    iban INTIGER NOT NULL,
                    customer_id INTIGER NOT NULL,
                    openDate text NOT NULL,
                    status text NOT NULL,
                    acctype text NOT NULL,
                    
                    FOREIGN KEY (customer_id)
                        REFERENCES CUSTOMERS (id)
                    
                )""")
    conn.commit()




def InsertCustomer (name,surname,dateofbirth):
    
    cur.execute("INSERT INTO CUSTOMERS (name,surname,dateofbirth) VALUES ( ? , ? , ?)" ,(name,surname,dateofbirth))
    conn.commit()

    return cur.lastrowid

def InsertAccount (iban,customer_id,openDate,status,acctype):
    
    cur.execute("INSERT INTO ACCOUNTS (iban,customer_id,openDate,status,acctype) VALUES ( ? , ? , ? , ? , ? )" ,(iban,customer_id,openDate,status,acctype))
    conn.commit()
    
    return cur.lastrowid


def getcustomer (customer_id):
    
    cur.execute("SELECT * FROM CUSTOMERS WHERE id = ?",(customer_id,))
    
    return cur.fetchone()

















































