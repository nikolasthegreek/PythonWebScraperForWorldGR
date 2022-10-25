from timeit import repeat
import HTMLManager

Letters=['Α','Β','Γ','Δ','Ε','Ζ','Η','Ι','Κ','Λ','Μ','Ν','Ξ','Ο','Π','Ρ','Σ','Τ','Υ','Φ','Χ','Ψ','Ω']
LetterCounter=0
WordCounter=850
LetterDone=False

DBArray=[]
memory=["","","","","","","","","",""]

def GetData(letter,incriment):
    return HTMLManager.GetData(letter,incriment).split("%")

data = GetData(Letters[LetterCounter],WordCounter)
while LetterCounter<= len(Letters):
    while not LetterDone:
        data = GetData(Letters[LetterCounter],WordCounter)
        i=0
        Sameword=True
        for datum in data:
            datum=datum.capitalize()
            if datum!=memory[i]:
                Sameword=False
            else:
                break
            if(len(datum)==5):
                    DBArray.append(datum)
            memory[i]=datum
            i+=1
        if Sameword:
            LetterDone=True
        print(WordCounter,data[-1],len(DBArray))
        WordCounter+=1
    print("done with ",Letters[LetterCounter]," starting with ",Letters[LetterCounter+1])
    LetterCounter+=1
    WordCounter=0
    LetterDone=False


