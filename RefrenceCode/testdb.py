import db_manager
import accounts
import customers
import sqlite3

conn = sqlite3.Connection('banking.db')
cur = conn.cursor()

def Initiate_Test_db():
    
    DeleteTables()
    
    db_manager.createtables()
    
    CreateTestdb()

def CreateTestdb ():
    
    cust = customers.CreateCustomer("Πετρος", "Παπαδοπουλος", "21/03/1981")
    accounts.CreateAccount(cust);
    accounts.CreateAccount(cust);
    
    cust = customers.CreateCustomer("Δημητρης", "Γιαννοπυλος", "07/12/1999")
    accounts.CreateAccount(cust);
    
    cust = customers.CreateCustomer("Γιαννης", "Λερος", "27/11/2001")
    
    cust = customers.CreateCustomer("Πετρος", "Παπαδοπουλος", "21/03/1981")
    accounts.CreateAccount(cust);
    
    cust = customers.CreateCustomer("Φιλιππος", "Βλαχος", "29/02/2001")
    accounts.CreateAccount(cust);
    
    cust = customers.CreateCustomer("Νικος", "Καραμανλης", "20/04/1967")
    accounts.CreateAccount(cust);
    
    cust = customers.CreateCustomer("Δημητρης", "Καραμολεγκου", "26/01/2003")
    accounts.CreateAccount(cust);
    
    cust = customers.CreateCustomer("jack", "daniels", "01/01/1921")
    accounts.CreateAccount(cust);
    accounts.CreateAccount(cust);
    accounts.CreateAccount(cust);
    
    
    
    conn.commit()
    
def DeleteTables ():
    
    cur.execute("""
                DROP TABLE IF EXISTS ACCOUNTS
                """)
    conn.commit()
    
    cur.execute("""
                DROP TABLE IF EXISTS CUSTOMERS
                """)
    conn.commit()

def ClearTables ():
    
    ("""
     DELETE * CUSTOMERS
     """)
    
    












































