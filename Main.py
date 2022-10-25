import HTMLManager

Letters=['Α','Β','Γ','Δ','Ε','Ζ','Η','Ι','Κ','Λ','Μ','Ν','Ξ','Ο','Π','Ρ','Σ','Τ','Υ','Φ','Χ','Ψ','Ω']
LetterCounter=0
WordCounter=5
LetterDone=False

def GetData(letter,incriment):
    return HTMLManager.GetData(letter,incriment).split("%")

data = GetData(Letters[LetterCounter],WordCounter)

for datum in data:
    print(datum)