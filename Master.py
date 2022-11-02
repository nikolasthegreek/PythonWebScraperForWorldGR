#from curses.ascii import HT
#code gave error not usere what this is (part of boilerplate)
from pickle import TRUE
from timeit import repeat

#initialasation of leters and progres
Letters=['Α','Β','Γ','Δ','Ε','Ζ','Η','Ι','Κ','Λ','Μ','Ν','Ξ','Ο','Π','Ρ','Σ','Τ','Υ','Φ','Χ','Ψ','Ω']
LetterCounter=0
PageCounter=0
LetterDone=False


#init of HTML manager

import HTMLManager
HTMLManager.LeterProgress=[Letters[LetterCounter],PageCounter]

#init of storage
import db_manager
db_manager.DeleteDB()
db_manager.createtables()
DBBuffer=[]
Memory=["","","","","","","","","",""]
WordCount=0

def UpdateProgress():
    HTMLManager.LeterProgress=[Letters[LetterCounter],PageCounter]
UpdateProgress()
while LetterCounter<= len(Letters):
    while not LetterDone:
        PageCounter+=1
        UpdateProgress()
        data = HTMLManager.GetData().split("%")
        if(data=="NULL"):
            LetterDone=TRUE
        else:
            i=0
            Sameword=True
            for datum in data:
                if datum!=Memory[i]:
                    Sameword=False
                else:
                    break
                if(len(datum)==5):
                        if (not("-"in datum)):
                            DBBuffer.append(datum)
                            WordCount=+1
                Memory[i]=datum
                i+=1
            if(len(DBBuffer)>=10):
                db_manager.InsertWords(DBBuffer)
                DBBuffer=[]
            if Sameword:
                LetterDone=True
        print(PageCounter,data[-1],WordCount)
    print("done with ",Letters[LetterCounter]," starting with ",Letters[LetterCounter+1])
    LetterCounter+=1
    PageCounter=0
    LetterDone=False
