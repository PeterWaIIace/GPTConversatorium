from bottle   import route, run
import threading
from conversation import ConversationRoom
import bottle
import json
import time
import os



config = {}
with open("config.json") as f:
    config = json.load(f)

Debate = ConversationRoom(config,"recording.html")
Debate.stop()

def runDebate():
    Debate.run()

_DebateThread = threading.Thread(target=runDebate)
_DebateThread.start()

conversation = False


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
    global Debate, _DebateThread

    personalityA  = bottle.request.json["A"]
    personalityB  = bottle.request.json["B"]
    with open("A.txt","w+") as f:
        f.write(personalityA)

    with open("B.txt","w+") as f:
        f.write(personalityB)

    Debate.start()

@bottle.post('/buttons/stop')
def buttonStart():
    global Debate, _DebateThread
    print("STOPPING")
    generate = False

    Debate.stop()
    _DebateThread.join()

run(host='localhost', port=8080, debug=True, quiet=False)