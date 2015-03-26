import requests
import commands
import time
import json

#Script to send live cricket score via iMessage or SMS (OSX only)
#TODO : figure out when the match has ended and stop spamming people.
def score():
    #currently the WC-15 semi finals url. Change it to the desired one.from http://cricscore-api.appspot.com/
    liveUrl="http://cricscore-api.appspot.com/csa?id=656493"
    #Copy the contact phone number from the contacts application
    buddyId="1234567890"
    didInterrupt = False
    print("Fetching matches..")
    dataFromUrl = requests.get(liveUrl)
    newscore = dataFromUrl.text
    json_data = json.loads(newscore)
    cur_score = json_data[0]['de']
    commands.getoutput('osascript sendsms.applescript '++'"'+cur_score+'"')
    time.sleep(60*5)

while True :
    score()
