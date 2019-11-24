import json

object = {"test1":"hello", "array": ["bring bring","boooop"]}

input = str(input("test1 or array? "))
if input == "array":
    inpu2 = input("0 or 1? ")
    inpu2 = str(inpu2)
    print(object["array"][inpu2])
else:
    print(object["test1"])

    #pipe spreadsheets to json objects. how do you want this set up?