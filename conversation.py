from pyGptBot import ChatBot as ChatBot
import subprocess
import os
import json
import time

class ConversationRoom:

    def __init__(self,GPTconfig,recording_filename):
        self.init_message = "Hello"

        # https://github.com/acheong08/ChatGPT/wiki/Setup

        self.chatGPT_1 =  ChatBot("A",organization=GPTconfig["organization"],apiKey=GPTconfig["apiKey"],personalityFile="A.txt")
        self.chatGPT_2 =  ChatBot("B",organization=GPTconfig["organization"],apiKey=GPTconfig["apiKey"],personalityFile="B.txt")

        self.filename = recording_filename

        self.__stop = True
        pass

    def updatePersonalities(self,GPTconfig):
        self.chatGPT_1 =  ChatBot("A",organization=GPTconfig["organization"],apiKey=GPTconfig["apiKey"],personalityFile="A.txt")
        self.chatGPT_2 =  ChatBot("B",organization=GPTconfig["organization"],apiKey=GPTconfig["apiKey"],personalityFile="B.txt")


    def update_file(self,gpt,message):
        with open(self.filename,"a") as f:
            scribe = "\n<li>\"Time\":\""+str(time.time())+"\"gpt\":\""+gpt+"\"message\":\""+message+"\"</li>\n"
            f.write(scribe)

    def start(self):
        self.__stop = False

    def stop(self):
        self.__stop = True

    def run(self):

        while(self.__stop):
            time.sleep(1)

        response = self.chatGPT_1.ask(self.init_message)
        self.update_file("A",response)
        while(not self.__stop):
            response = self.chatGPT_1.ask(response)
            self.update_file("B",response)
            response = self.chatGPT_1.ask(response)
            self.update_file("A",response)



