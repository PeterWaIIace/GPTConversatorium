from revChatGPT.revChatGPT import Chatbot
import subprocess
import os
import json
import time

class ConversationRoom:

    def __init__(self,firstGPT_config,secondGPT_config,recording_filename):
        self.init_message = "Start Conversation"

        # https://github.com/acheong08/ChatGPT/wiki/Setup

        self.chatGPT_1 =  Chatbot(firstGPT_config, conversation_id=None)
        self.chatGPT_2 =  Chatbot(secondGPT_config, conversation_id=None)

        self.filename = recording_filename
        pass


    def update_file(self,gpt,message):
        with open(self.filename,"a") as f:
            scribe = "\n{\"Time\":\""+str(time.time())+"\"gpt\":\""+gpt+"\"message\":\""+message+"\"}\n"
            f.write(scribe)

    def run(self):

        response = self.chatGPT_1.get_chat_response(self.init_message, output="text")["message"]
        self.update_file("gpt1",response)
        while(True):
            response = self.chatGPT_2.get_chat_response(response, output="text")["message"]
            self.update_file("gpt2",response)
            response = self.chatGPT_1.get_chat_response(response, output="text")["message"]
            self.update_file("gpt1",response)


config_1 = {
    "email":"PW4ltz@proton.me",
    "password": "DXE8q#1*mBqsLFDtj$mQ"
}

config_2 = {
    "email":"PW4ltz@proton.me",
    "password": "DXE8q#1*mBqsLFDtj$mQ"
}

# returns {'message':message, 'conversation_id':self.conversation_id, 'parent_id':self.parent_id}
generator = ConversationRoom(config_1,config_2,"recording.txt")
generator.run()