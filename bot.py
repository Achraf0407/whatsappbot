# File: bot.py

import openai
from twilio.rest import Client

# Twilio account information
account_sid = '<AC41e60380cabb2306283d46d9c746429c>'
auth_token = '<313046749e1f9a44e01feafb6116f2d0>'
client = Client(account_sid, auth_token)

# OpenAI API Key
openai.api_key = "<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>"

def process_message(message):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt='<user_message> ' + message,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response["choices"][0]["text"]

def receive_message():
    messages = client.messages.list(to="whatsapp:<+14155238886>")
    for message in messages:
        if message.from_ != "whatsapp:<+14155238886>":
            response = process_message(message.body)
            send_message(message.from_, response)

def send_message(to, message):
    message = client.messages.create(
        to=to,
        from_="whatsapp:<+14155238886>",
        body=message
    )

if __name__ == '__main__':
    receive_message()
