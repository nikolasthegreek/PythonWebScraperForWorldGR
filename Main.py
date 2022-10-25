import HTMLManager


Letters=['Α','Β','Γ','Δ','Ε','Ζ','Η','Ι','Κ','Λ','Μ','Ν','Ξ','Ο','Π','Ρ','Σ','Τ','Υ','Φ','Χ','Ψ','Ω']
LetterCounter=0
WordCounter=0
LetterDone=False

print("feching")
htmlitem=HTMLManager.GetHTML(Letters[LetterCounter],WordCounter)
print("parsing")

Segments= htmlitem.split("<dl")
del Segments[:1]
Segments[-1]=Segments[-1].split("</dl>")[1]

print("done")

while not LetterDone :
    break