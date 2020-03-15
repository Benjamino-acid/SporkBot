import sys, json, requests
from re import sub

def return_help():
    print("Define Help")
    print("This will return the definition(s) of a word")
    print("\tUsage: /spork define [word]")

if (len(sys.argv) < 1) or (sys.argv[1].lower() == "help"):
    print(return_help())

else:
    word = sys.argv[1]
    overall = (requests.get("https://dictionaryapi.com/api/v3/references/collegiate/json/" + word + "?key=499694fe-5b83-46cf-b61f-53448229592f"))

    print(overall)
