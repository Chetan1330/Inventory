from email import header
import json
import os
import sys

def getToken():
    file = open("token.txt", "r")
    return file.read()

def setToken(token):
    try:
        file = open("token.txt", "w")
        file.write(token)
        return True
    except:
        return False

def getHeaders():
    headers={
        "accept":"application/json",
        "Authorization":"Bearer"+json.loads(getToken())["token"]
    }
    return headers 
