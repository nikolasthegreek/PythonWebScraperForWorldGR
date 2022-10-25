from turtle import done
import requests

def GenLink (letter,incriment):
    return "https://www.greek-language.gr/greekLang/modern_greek/tools/lexica/triantafyllides/search.html?start={}&lq={}*&dq=".format(incriment*10,letter)

def GetHTML(letter,incriment):
    return requests.get(GenLink(letter,incriment)).text
def GetData(letter,incriment):
    print("feching")
    htmlitem=GetHTML(letter,incriment)
    print("parsing")

    Segments= htmlitem.split("<dl")
    del Segments[:1]
    Segments[-1]=Segments[-1].split("</dl>")[0]
    i=0
    for segment in Segments:
        Segments[i]=segment.split("<b>")[1].split("</b>")[0]
        i+=1

    i=0
    for segment in Segments:
        Segments[i]=segment.split(" ")[0]
        i+=1
    print("done")
    return "%".join(Segments)
