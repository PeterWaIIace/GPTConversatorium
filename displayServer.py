from bottle import route, run, template,static_file
import json

@route('/chat')
def index():
    data = []
    with open("recording.json","r") as f:
        data = f.read()
        with open("recording_copy.json","w") as f_copy:
            f_copy.write(data)
            f_copy.write("}")

    return static_file("recording_copy.json", root='.', mimetype='application/json')

@route('/getConversation', method='GET')
def index():
    data = []
    with open("recording.json","r") as f:
        data = f.read()
        with open("recording_copy.json","w") as f_copy:
            f_copy.write(data)
            f_copy.write("}")

            data = json.load(f_copy)

    return "OK"

run(host='localhost', port=8080)