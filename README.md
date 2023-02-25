# GPTConversatorium
Let GPT talk to itself!

![image](https://user-images.githubusercontent.com/40773550/221324934-3e3ece4d-8ef8-4bbb-8ce1-d5f47b2d7d84.png)


This repository uses reversed engineered GPT API library revChatGPT. To start using it, open source code and change these two configs:

```
config_1 = {
    "email":"*",
    "password": "*"
}

config_2 = {
    "email":"*",
    "password": "*"
}
```

after that run conversation.py, and you will see recordings of it inside txt file.

Recoding output is json file: 
```
{index:{"Time":<time>,"gpt":<ai_name>,"message":<message from ai>}}
```
You can view recording by running:
```
python displayServer.py
```
and accessing: `localhost:8080\chat`

Example recording:

![image](https://user-images.githubusercontent.com/40773550/206881115-fa549192-799f-49b6-a873-161f999018e3.png)
