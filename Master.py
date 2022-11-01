#from curses.ascii import HT
#code gave error not usere what this is (part of boilerplate)
from pickle import TRUE
from timeit import repeat

#initialasation of leters and progres
Letters=['Α','Β','Γ','Δ','Ε','Ζ','Η','Ι','Κ','Λ','Μ','Ν','Ξ','Ο','Π','Ρ','Σ','Τ','Υ','Φ','Χ','Ψ','Ω']
LetterCounter=0
WordCounter=0
LetterDone=False


#init of HTML manager

import HTMLManager
HTMLManager.LeterProgress=[Letters[LetterCounter],WordCounter]

#definiton of storage

DBArray=[]
memory=["","","","","","","","","",""]

def UpdateProgress():
    HTMLManager.LeterProgress=[Letters[LetterCounter],WordCounter]
UpdateProgress()
while LetterCounter<= len(Letters):
    while not LetterDone:
        WordCounter+=1
        UpdateProgress()
        data = HTMLManager.GetData().split("%")
        if(data=="NULL"):
            LetterDone=TRUE
        else:
            i=0
            Sameword=True
            for datum in data:
                if datum!=memory[i]:
                    Sameword=False
                else:
                    break
                if(len(datum)==5):
                        if (not("-"in datum)):
                            DBArray.append(datum)
                memory[i]=datum
                i+=1
            if Sameword:
                LetterDone=True
        print(WordCounter,data[-1],len(DBArray))
    print("done with ",Letters[LetterCounter]," starting with ",Letters[LetterCounter+1])
    LetterCounter+=1
    WordCounter=0
    LetterDone=False
