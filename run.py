from bottle   import route, run
import threading
from conversation import ConversationRoom
import bottle
import json
import time
import os

def cleanFiles():
    with open("A.txt","w+") as f:
        f.write("")

    with open("B.txt","w+") as f:
        f.write("")

    with open("personA.txt","w+") as f:
        f.write("")

    with open("personB.txt","w+") as f:
        f.write("")
cleanFiles()

config = {}
with open("config.json") as f:
    config = json.load(f)

Debate = ConversationRoom(config,"recording.html")

def runDebate():
    Debate.run()

print("thread started!")
# conversation = False

@bottle.route('/')
def index():
    root = os.path.join(os.path.dirname(__file__), 'frontEnd')
    return bottle.static_file('index.html', root=root)

@bottle.route('/<filename>')
def interfaces(filename="index.js"):
    root = os.path.join(os.path.dirname(__file__), 'frontEnd')
    return bottle.static_file(filename, root=root)

@bottle.route('/readConversation')
def readJson():
    response = bottle.static_file("recording.html", root='')
    response.set_header("Cache-Control", "public, max-age=1")
    return response

@bottle.post('/buttons/start')
def buttonStart():
    global Debate, _DebateThread,config

    personalityA  = bottle.request.json["A"]
    personalityB  = bottle.request.json["B"]
    nameA  = bottle.request.json["A"]
    nameB  = bottle.request.json["B"]

    with open(f"{nameA}.txt","w+",encoding="utf-8") as f:
        f.write(personalityA)

    with open(f"{nameB}.txt","w+",encoding="utf-8") as f:
        f.write(personalityB)

    Debate.updatePersonalities(config,nameA,nameB)
    Debate.start()

@bottle.post('/buttons/stop')
def buttonStart():
    global Debate, _DebateThread
    print("STOPPING")

    Debate.stop()
    _DebateThread.join()

if __name__=="__main__":
    Debate.stop()
    _DebateThread = threading.Thread(target=runDebate)
    _DebateThread.start()
    run(host='localhost', port=8088, debug=False, quiet=True)
    Debate.stop()
    _DebateThread.join()
