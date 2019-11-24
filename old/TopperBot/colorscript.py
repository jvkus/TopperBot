from googleapiclient import errors, discovery
from oauth2client.contrib import gce
from sheetsauth import get_credentials
from colorutils import Color, hex_to_hsv, hsv_to_hex, hsv_to_rgb
from quicksort2 import quicksort as qs
import httplib2
import numpy as np

colors = []

#REPLACE ALL THIS WITH A DATABASE#
#BUG: YOUR RESULTS ARE NOT BEING CHANGED EACH TIME.#

#Global variables that store the closest colors. Remember to reset these to NULL once they're spit back out
#on Discord.
#Basic information needed to connect to the spreadsheets.
SCOPES = "https://www.googleapis.com/auth/spreadsheets"
SECRET_FILE = "client_secret.json"
APPLICATION_NAME = 'Google Sheets API'
PSHEET = "colorpalettes"
spreadsheetId = "*********"

credentials = get_credentials()
service = discovery.build("sheets", "v4", credentials=credentials)
request = service.spreadsheets().values().batchGet(spreadsheetId=spreadsheetId)
response = request.execute

http = credentials.authorize(httplib2.Http())
sheets = discovery.build("sheets", "v4", http=http)

#Finds color in spreadsheet closest to input value.#
#def color(hexinput, ):
    #split hexinput in hex tuple.
    #it has come to my attention that HSL is better than RGB/hex.
    #CIELUV or Lab* is better than HSL
    #create a function that runs through all values
    #pull all values

    # THIS ALGORITHM ACTUALLY IS PRETTY INACCURATE.
def colorsub(val,col):      #Short for color subtract. Calculates closeness of different colors.
    result = [0,0,0]
    sum = 0
    for i in range(0,3):    #This repeats for all three of the values in an HSV triple.
        if val[i]>=col[i]:
            result[i] = round(np.subtract(val[i], col[i]), 3)  #Subtracts and rounds the result to two digits.
        else:
            result[i] = round(np.subtract(col[i], val[i]), 3)
    for i in range(0,3):
        sum = sum + result[i]
    return sum

#cpal is the name of the color palette sheet to be converted.
#This method is crap. Rewrite to work with a JSON file.
#Additionally, you'll need to convert your spreadsheet to JSON. This should be simple.
#Write a script that gets data from spreadsheets, pulls the sheet name for the new JSON object, stores the
#cell coordinates as the location in the 

#LIMIT numOfColorsToReturn TO MAXIMUM 50 OUTPUT TO PREVENT SYSTEM OVERLOAD.
def findcolor(colorInput, numOfColorsToReturn, cpal):
    global colors                           #This array stores the compared values.
    rnge = cpal + "!A1:E18"                 #Done to fetch all colors from a specific color palette.
    colorInput = hex_to_hsv(colorInput)     #Converts hex value of the input color value to HSV.
    values = sheets.spreadsheets().values().get(range=rnge,spreadsheetId=spreadsheetId).execute().get("values")

    if(cpal != "Default"):              #This runs for all sets besides the starting set of just one column.
        for i in range(0,18):           #Repeats for every row.
            newarray = []               #Temporarily stores values of results from j loop.
            for j in range(0,5):        #Repeats for every column.
                valhsv = hex_to_hsv(values[i][j])
                result = colorsub(valhsv, colorInput)
                newarray.append(result)
            colors.append(newarray)
    else:
        for i in range(0,18):
            valhsv = hex_to_hsv(values[i])
            result = colorsub(valhsv, colorInput)
            colors.append(result)

    maxVal = 500    #This value is used to deduce the smallest differences.
    results = []
    
    #RETHINK YOUR LOGIC.

    #actually this is bad. just sort the garbage first and throw out everything after the first x.
    #why not just sort the entire list and then 
    '''if(cpal != "Default"):  #These loops compare the results to find the top x (x = numOfColorsToReturn).
        for i in range(0, 18):
            for j in range(0, numOfColorsToReturn):
                newArray2 = []
                newArray2.append(colors[i][j])
                newArray2.append(i)
                newArray2.append(j)
                if(len(results) < numOfColorsToReturn):
                    results.append(newArray2)
                else:
                    tempValue = results[0][0]
                    tempIndex = 0
                    for l in range(0, numOfColorsToReturn):
                        if(tempValue < results[l][0]):
                            tempValue = results[l][0]
                            tempIndex = l
                    if(colors[i][j] < tempValue):
                        results[tempIndex][0] = colors[i][j]
                        results[tempIndex][1] = i
                        results[tempIndex][2] = j

    else:
        for i in range(0, 18):
            newArray2 = []
            newArray2.append(colors[i])
            if(len(results) < numOfColorsToReturn):
                results.append(newArray2)
            else:
                tempValue = results[0][0]
                tempIndex = 0
                for l in range(0, numOfColorsToReturn):
                    if(tempValue < results[l][0]):
                        tempValue = results[l][0]
                        tempIndex = l
                if(colors[i] < tempValue):
                    results[tempIndex][0] = colors[i]
                    results[tempIndex][1] = i'''



    resultSort = []
    for i in range(0, numOfColorsToReturn):
        resultSort.append(results[i][0])

    resultSort = qs(resultSort)   #Quicksorts the list.

    for i in range(0, len(results)):    #Converts the list type to a number. Doesn't want to work otherwise.
        results[i][0] = float(results[i][0])
        results[i][1] = int(results[i][1])
        results[i][2] = int(results[i][2])

    coordinate = " "
    for i in range(0, numOfColorsToReturn):
        for j in range(0, numOfColorsToReturn):
            if results[i][0] == resultSort[j]:
                    resultSort[j] = results[i]
        coordinate = chr(results[i][2] + 65)
        coordinate = coordinate + str(results[i][1])
        results[i][1] = coordinate
        coordinate = cpal + "!" + coordinate
        results[i][0] = sheets.spreadsheets().values().get(range=coordinate,spreadsheetId=spreadsheetId).execute().get("values")[0][0]  #ALL THIS WILL HAVE TO CHANGE WITH A 
        results[i].remove(results[i][2])

    return results