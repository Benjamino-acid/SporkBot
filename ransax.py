import sys, json
from requests import get
from re import sub
from random import randint

def return_help():
    print("Random Sax Help")
    print("This will return a random Sax Squatch video")
    print("\tUsage: /spork ransax ")

if (len(sys.argv) < 1) or (sys.argv[1].lower() == "help"):
    print(return_help())

else:
    word = sys.argv[1]
    response = get("https://www.googleapis.com/youtube/v3/search?key=AIzaSyA5ZV5v_mBBwN9ch8tyRq1h4r7DgSl4ZcQ&channelId=UCsk4ifMbqblkpB8gidE-97g&part=snippet,id&order=date&maxResults=50")
    j = response.json()
    
    vList = []
    vTitles = []

    for item in j['items']:
        try:
            vId = item["id"]["videoId"]
            vTitle = item["snippet"]["title"]
            
            vList.append(vId)
            vTitles.append(vTitle)
            
            #print(vId)
            #print(vTitle)
        except KeyError:
            continue
        except UnicodeEncodeError:
            continue
    
    cnt = len(vList)

    randIndex = randint(0, cnt-1)
    #print(randIndex)

    url = "https://www.youtube.com/watch?v=" + vList[randIndex]
    title = vTitles[randIndex]

    #print(url, title)

    print(url)
    #print("<a href='" + url  + "' >" + title  + "</a>")
