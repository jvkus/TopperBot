from __future__ import print_function
from googleapiclient import errors, discovery
from oauth2client.contrib import gce
from sheetsauth import get_credentials
from PIL import ImageColor

import io
import httplib2
import os
import pandas as pd
import numpy.random as rand 
import matplotlib as mpl
import matplotlib.pyplot as plt

#remove imports if I turn out to actually not need any of them#
#There is a limit of 1k calls per batch request. If more calls are necessary, use more batch reqs.#
#Sheet stores edited responses separately. Check for multiples under the same name and call the most recent timestamp.#

SCOPES = "https://www.googleapis.com/auth/spreadsheets.readonly"
SECRET_FILE = "client_secret.json"
APPLICATION_NAME = 'Google Sheets API'
SHEET = "Copy of projects inventory"
PSHEET = "colorpalettes"
#be sure to change this back to the original one once bugs are worked out so you have current data.#
#spreadsheetId = "**********" <- this is the placeholder
spreadsheetId = "**********"
palettesheetId = "**********"

credentials = get_credentials()
service = discovery.build("sheets", "v4", credentials=credentials)
request = service.spreadsheets().values().batchGet(spreadsheetId=spreadsheetId)
response = request.execute

http = credentials.authorize(httplib2.Http())
sheets = discovery.build("sheets", "v4", http=http)

#questions = sheets.spreadsheets().values().get(range="1",spreadsheetId=spreadsheetId).execute().get("values")
#namestimes = sheets.spreadsheets().values().get(range="C:C",spreadsheetId=spreadsheetId).execute().get("values")

#print(namestimes)  

def findusers(item, question):
    result = []
    stor = []
    x = 30
    #x = "WRITE CODE THAT READS AMOUNT OF ROWS IN SPREADSHEET"
    #include stuff for sigil, color palettes, armor, syandana#
    #This should be trashed and replaced with a sqlite db.#
    if question=="warframe":
        for i in range(0,x): #THIS IS BROKEN UNTIL YOU WRITE CODE FOR X.#
            result.append(["0","1","2"])
            rangeid = [("A" + str(i+1)),("B" + str(i+1)),("D" + str(i+1))]
            result[i][2] = sheets.spreadsheets().values().get(range=rangeid[2],spreadsheetId=spreadsheetId).execute().get("values")
            result[i][1] = sheets.spreadsheets().values().get(range=rangeid[1],spreadsheetId=spreadsheetId).execute().get("values")
            result[i][0] = sheets.spreadsheets().values().get(range=rangeid[0],spreadsheetId=spreadsheetId).execute().get("values")
    for i in range(0,x):
        searchitem = item + ","
        if searchitem in result[i][2]:
            result.remove(result[i])
    for i in range(0,len(result)):
        stor.append(result[i][1])
    endresult = "\n".join(stor)
    return endresult
        #instead of doing things like... item, question arguments, compress those queries into one argument. such as...
        #warframe:volt
        #or sigil:grustrag . then you get information from that :^)
        #search for item in the array and pop out the values from the array that don't have what you're looking for.

'''So. Some notes. For the screenshot reader, you will have to store the data somehow.
Use something like MongoDB or JSON databases.
Pitfall for operator hair: Because it is unnamed, you will have to ask the user a
question for each style, flashing an image and asking if they have it. This should only
take them a minute.

How will you sort out text from the screenshots? Look for " [" and store the words
before it. Because OCR grabs text from boxes, you can just look for the text items
in the object and grab each item with " [" and store that. At least... That's what will
work for weapons and Warframes.
As for armor, sentinels, whatnot... Look for "syandana" or "plate" or "chest" or
"mask". All sorts of keywords. Operator will be a fucker.
You're going to have to keep track of keywords for each and every type of keyword.
" [" also works for companions, sentinels, and sentinel weapons.

Perhaps you will have to do the following:
- Query for certain type of item.
- Catch it by the keyword.
- Store it.

Items will not be lumped together in nearly as many sections as they are on the form.
Instead, they will be appropriately sorted into large sections. Here's what I'm
thinking: Warframes/Archwings/weapons, companions/sentinels/sentinel weapons, Warframe
cosmetics (huge section that encompasses armor, syandanas, Warframe skins, all regalia,
helmets, auxiliary cosmetics, weapon skins, Archwing cosmetics, and animation sets),
companion/sentinel cosmetics (includes armor and skins), color palettes, landing
crafts, landing craft skins, Operator hairstyles, Operator cosmetics (includes suits
and additional accessories), glyphs. This totals up to ten categories.
You also need to store mastery rank and Stratos emblem number.
'''

#Call all online with x roles who have certain cosmetics.#

#Who has x item?#

#List popularity of certain items.#

#How many people have this vs. this?#

#Add some functions to sort between who is and isn't online.#

#Bar graph of how popular each item is.#

##COLOR FUNCTIONS##
#Pick random colors with x palettes.#

#Pick a few closest colors on x palettes (or all, if unspecified) to a specified hex code. Bonus: pick average from an image.#

#Change bot profile picture.#

#Change bot nickname.#

#Disable above two functions for certain roles.#

##ORGANIZATIONAL FUNCTIONS##
#NEEDS DATABASE FOR THIS INFORMATION.#
#Only creator can access files on projects they create. Can also give read, add, and delete/overwrite permissions to other users.#
#Create backups of old versions that last a week.#

#List projects.#

#Add notes to project.#

#Maybe create web UI to go with this?#