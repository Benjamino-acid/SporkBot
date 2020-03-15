import sys, json
from requests import get
from re import sub

def return_help():
    print("Define Help")
    print("This will return the definition(s) of a word")
    print("\tUsage: /spork define [word]")

if (len(sys.argv) < 1) or (sys.argv[1].lower() == "help"):
    print(return_help())

else:
    word = sys.argv[1]
    response = get("https://dictionaryapi.com/api/v3/references/collegiate/json/" + word + "?key=499694fe-5b83-46cf-b61f-53448229592f")
    j = response.json()

    print(word.upper())
    
    for df in j[0]['def']:
        for sq in df['sseq']:
            try:
                d = sq[0][1]['dt'][0][1]
                d = d.replace('{bc}','')
                d = sub(r'{[a-z]+\|','', d)
                d = d.replace('||}','')
                print(d)
            except KeyError:
                continue

    print("For more details, visit:")
    print("https://www.dictionary.com/browse/" + word + "?s=t")
