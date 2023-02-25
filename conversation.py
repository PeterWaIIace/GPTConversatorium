from pyGptBot import ChatBot as ChatBot
import subprocess
import os
import json
import time

class ConversationRoom:

    def __init__(self,GPTconfig,recording_filename,botNameA="personA",botNameB="personB",length=100):
        self.init_message = "Hello"

        # https://github.com/acheong08/ChatGPT/wiki/Setup

        self.length = length

        self.botNameA = botNameA
        self.botNameB = botNameB

        self.chatGPT_1 =  ChatBot(self.botNameA,organization=GPTconfig["organization"],apiKey=GPTconfig["apiKey"],personalityFile=f"{self.botNameA}.txt",debug=True)
        self.chatGPT_2 =  ChatBot(self.botNameB,organization=GPTconfig["organization"],apiKey=GPTconfig["apiKey"],personalityFile=f"{self.botNameB}.txt",debug=True)

        self.filename = recording_filename

        self.__stop = True
        pass

    def updatePersonalities(self,GPTconfig):
        self.chatGPT_1 =  ChatBot(self.botNameA,organization=GPTconfig["organization"],apiKey=GPTconfig["apiKey"],personalityFile=f"{self.botNameA}.txt")
        self.chatGPT_2 =  ChatBot(self.botNameB,organization=GPTconfig["organization"],apiKey=GPTconfig["apiKey"],personalityFile=f"{self.botNameB}.txt")


    def update_file(self,gpt,message):
        with open(self.filename,"a",encoding="utf-8") as f:
            scribe = f"\n<li>{message}</li>\n"
            f.write(scribe)

    def start(self):
        with open(self.filename,"w",encoding="utf-8") as f:
            f.write("")
        self.__stop = False

    def stop(self):
        self.__stop = True

    def run(self):

        counter = 0

        while(self.__stop):
            time.sleep(1)

        response = self.chatGPT_1.ask(self.init_message)
        self.update_file(self.botNameA,response)

        while(not self.__stop and self.length > counter):

            response = self.chatGPT_2.ask(response)
            self.update_file(self.botNameB,response)

            response = self.chatGPT_1.ask(response)
            self.update_file(self.botNameA,response)

            counter+=1



