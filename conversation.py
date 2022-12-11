from revChatGPT.revChatGPT import Chatbot
import subprocess
import os
import json
import time

class ConversationRoom:

    def __init__(self,firstGPT_config,secondGPT_config,recording_filename,time_in_minutes=10):
        self.init_message = "I want you to have respond to another AI. You are allowed to make or change topic if responses are repeating. I will send you its inputs as messages and you will respond."+\
                            "Please ask random question to start conversation:"

        # https://github.com/acheong08/ChatGPT/wiki/Setup

        self.chatGPT_1 =  Chatbot(firstGPT_config, conversation_id=None)
        self.chatGPT_2 =  Chatbot(secondGPT_config, conversation_id=None)

        self.filename = recording_filename
        self.time_in_minutes = time_in_minutes*60
        self.index = 0
        with open(self.filename,"w") as f:
            scribe = "{"
            f.write(scribe)
        pass


    def update_file(self,gpt,message):
        with open(self.filename,"a") as f:
            scribe = "\n\""+str(self.index)+"\":{\"Time\":\""+str(time.time())+"\",\"gpt\":\""+gpt+"\",\"message\":\""+message.replace("\n", " ")+"\"}"
            if self.index != 0:
                scribe = ","+scribe
            f.write(scribe)
            self.index+=1

    def run(self):

        response = self.chatGPT_1.get_chat_response(self.init_message, output="text")["message"]
        self.update_file("gpt1",response)

        t_start = time.time()
        while(self.time_in_minutes > (time.time() - t_start)):
            response = self.chatGPT_2.get_chat_response("gpt2: "+response, output="text")["message"]
            self.update_file("gpt2",response)
            response = self.chatGPT_1.get_chat_response("gpt1: "+response, output="text")["message"]
            self.update_file("gpt1",response)

        with open(self.filename,"a") as f:
            scribe = "\n}"
            f.write(scribe)


config_1 = {
    "email":"*",
    "password": "*"
}

config_2 = {
    "email":"*",
    "password": "*"
}

# returns {'message':message, 'conversation_id':self.conversation_id, 'parent_id':self.parent_id}
generator = ConversationRoom(config_1,config_2,"recording.json",10)
generator.run()