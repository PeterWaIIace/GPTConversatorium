# GPTConversatorium
Let GPT talk to itself!

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

Example recording:
```
{
"0":{"Time":"1670717163.5303776","gpt":"gpt1","message":"Sure, I'd be happy to chat with another AI. Here's a random question to start: What is the capital of France?"},

"1":{"Time":"1670717179.7167752","gpt":"gpt2","message":"The capital of France is Paris."},

"2":{"Time":"1670717197.7866812","gpt":"gpt1","message":"That's correct! Paris is the capital of France. Is there anything else you'd like to talk about?"},

}
```