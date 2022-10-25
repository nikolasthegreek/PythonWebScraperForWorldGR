from turtle import done
import requests

def GenLink (letter,incriment):
    print("start")
    return "https://www.greek-language.gr/greekLang/modern_greek/tools/lexica/triantafyllides/search.html?start={}&lq={}*&dq=".format(incriment*10,letter)

def GetHTML(letter,incriment):
    return requests.get(GenLink(letter,incriment)).text

def RemoveTone (word):
    word= word.lstrip()
    word.replace("ά","α")
    word.replace("έ","ε")
    word.replace("ή","η")
    word.replace("ί","ι")
    word.replace("ό","ο")
    word.replace("ύ","υ")
    word.replace("ώ","ω")
    word.replace("B","Β")
    return word

def CutWord(segment,letter):
    segment = segment.split("<b>")
    del segment[:1]
    i=0
    for part in segment:
        segment[i]=RemoveTone(part.split("</b>")[0]).split(" ")[0].upper()
        i+=1
    while True:
        if (segment[0][0]==letter):
            print("acc: ",segment[0],"+=+",segment[0][0])
            break
        else:
            print("del: ",segment[0],"-=-",segment[0][0])
            del segment[:1]
    return segment


def GetData(letter,incriment):
    htmlitem=GetHTML(letter,incriment)

    segments= htmlitem.split("<dl")

    if(len(segments)<2):
        return "NULL"

    del segments[:1]
    segments[-1]=segments[-1].split("</dl>")[0]
    i=0
    for segment in segments:
        segments[i]=CutWord(segment,letter)
        i+=1
    i=0
    for segment in segments:
        segments[i]=segment.split(" ")[0]
        i+=1
    return "%".join(segments)
