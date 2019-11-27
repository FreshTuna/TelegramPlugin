import os
import sys

from time import sleep
from telethon.tl.custom.sendergetter import SenderGetter
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.types import (
PeerChannel
)
from telethon.tl.functions.messages import GetHistoryRequest
from telethon import TelegramClient, events, sync
from telethon.tl.types.contacts import Contacts
from telethon.tl.functions.contacts import GetContactsRequest
from telethon.tl.types import InputPeerUser
api_id = 474030
api_hash = '56be342c1ace1f9509ca1e1d920eed5e'
phone_number = '+821084125070'
client = TelegramClient('jang', api_id, api_hash)
client.start(phone_number)

#client.send_message('jangjunyoung','Hello!')

messages = client.get_messages('jangjunyoung')
print(messages[0].message)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone_number)
    client.sign_in(phone_number, input('Enter code : '))

contact_list = {
}

contacts = client(GetContactsRequest(0))
print(contacts)

for u in contacts.users:
     client.send_message(InputPeerUser(u.id, u.access_hash),"hi")
     contact_list[u.id] = u.access_hash
     print(contact_list[u.id])

invite_link = 'https://t.me/ASDFZCXV'

user_input_channel = invite_link

if user_input_channel.isdigit():
    entity = PeerChannel(int(user_input_channel))
else:
    entity = user_input_channel

my_channel = client.get_entity(invite_link)
print(my_channel)

channel_entity=client.get_entity(invite_link)
posts = client(GetHistoryRequest(
    peer=channel_entity,
    limit=100,
    offset_date=None,
    offset_id=0,
    max_id=0,
    min_id=0,
    add_offset=0,
    hash=0
    ))

for message in posts.messages:
    print(message)
    print(message.message)

message_10 = client.get_me()
print(message_10)
channel ='ASDFZCXV'
channels = {d.entity.username: d.entity
            for d in client.get_dialogs()
            if d.is_channel}
channel = channels[channel]
print(channel)
for u in client.iter_participants(channel, aggressive=True):
  print(u.id, u.first_name, u.last_name, u.username)

current_sentence = ""
banned_word="Âü¿Ü"
error_sentence = "dont say"+banned_word+"please"
async def main():
    chat =await client.get_input_entity('Shit')
    print("Received Data!!")
    async for messages in client.iter_messages(chat):
        current_sentence=messages.message
        if current_sentence == None:
            break
        print(messages.from_id," : ",current_sentence)
        if current_sentence.find(banned_word) ==0 :
            print(current_sentence.find(banned_word))
            print("he said ",banned_word)
            await client.send_message(InputPeerUser(messages.from_id, contact_list[messages.from_id]),
                                      error_sentence)

while True :
    with client:
        client.loop.run_until_complete(main())
        sleep(30)