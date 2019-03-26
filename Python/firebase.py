import urllib.request
import json
import os


def getDicionario () :
    try:
        with open('dicionario.json') as data_file:    
            #response = urllib.request.urlopen('/dicionario.json')
            data = json.load(data_file) 
            return data
    except Exception as e:
        print(e)
dicionario = getDicionario()
