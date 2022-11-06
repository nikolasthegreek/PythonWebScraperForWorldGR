from doctest import master
from pickle import TRUE
import re
from turtle import done
import requests

def GenLink (letter,incriment):
    return "https://www.greek-language.gr/greekLang/modern_greek/tools/lexica/triantafyllides/search.html?start={}&lq={}*&dq=".format(incriment*10,letter)

def GetHTML(letter,incriment):
    return requests.get(GenLink(letter,incriment)).text
Buffer=["",""]
BufferStat=True
LeterProgress=[]
#BufferStat shows if the buffer is up to date, if the site takes too long and the program prosesed the html
#faster than it can get the html BufferStat tells it to wait for the HTML to arive
BufferSel=True
#BufferSel indicates if it is the first to read 0 false 1 true
BufferEmpty=True
#indicates if the buffer is nemty

def BufferIncreament():
    global BufferSel
    BufferSel=not BufferSel

def BufferWrite():
    global BufferStat,Buffer
    if(BufferSel):
        Buffer[0]=(GetHTML(LeterProgress[0],LeterProgress[1]))
        #this is were threading should happen
    else:
        Buffer[1]=(GetHTML(LeterProgress[0],LeterProgress[1]))
        #this is were threading should happen
    BufferStat=True
    return

def BufferGetData():
    global Buffer,BufferSel
    if(BufferSel):
        return Buffer[1]
    else:
        return Buffer[0]

def BufferRead():
    global BufferStat,BufferEmpty
    if(BufferEmpty):
        BufferWrite()
        BufferIncreament()
    if(BufferStat):
        BufferStat=not BufferStat
    else:
        while(not BufferStat):
            BufferStat=not BufferStat
    BufferWrite()
    BufferIncreament()
    return BufferGetData()

def RemoveTone (word):
    word= word.lstrip()
    word=word.replace("ά","α")
    word=word.replace("έ","ε")
    word=word.replace("ή","η")
    word=word.replace("ί","ι")
    word=word.replace("ό","ο")
    word=word.replace("ύ","υ")
    word=word.replace("ώ","ω")
    return word

def CutWord(segment,letter):
    segment = segment.split("<b>")
    del segment[:1]
    i=0
    for part in segment:
        segment[i]=RemoveTone(part.split("</b>")[0]).split(" ")[0]
        if(len(segment[i])==0):
            return "NULL"
        if(segment[i][0].isupper()):
            segment[i]=segment[i].replace(segment[i][0],letter)
        segment[i]=segment[i].upper()
        i+=1
    while True:
        if (segment[0][0]==letter):
            break
        else:
            del segment[:1]
        if(len(segment)==0):
            return "NULL"
    return segment[0]


def GetData():
    htmlitem=BufferRead()

    segments= htmlitem.split("<dl")

    if(len(segments)<2):
        return "NULL"

    del segments[:1]
    segments[-1]=segments[-1].split("</dl>")[0]
    i=0
    for segment in segments:
        segments[i]=CutWord(segment,LeterProgress[0])
        i+=1
    i=0
    for segment in segments:
        segments[i]=segment.split(" ")[0]
        i+=1
    return "%".join(segments)
