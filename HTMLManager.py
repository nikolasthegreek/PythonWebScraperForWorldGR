import requests

def GenLink (letter,incriment):
    return "https://www.greek-language.gr/greekLang/modern_greek/tools/lexica/triantafyllides/search.html?start={}&lq={}*&dq=".format(incriment,letter)

def GetHTML(letter,incriment):
    return requests.get(GenLink(letter,incriment)).text

