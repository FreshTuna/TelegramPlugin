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
from telethon.tl.functions.channels import JoinChannelRequest
from telethon import TelegramClient, events, sync
from telethon.tl.types.contacts import Contacts
from telethon.tl.functions.contacts import GetContactsRequest
from telethon.tl.types import InputPeerUser

api_id = 474030
api_hash = '56be342c1ace1f9509ca1e1d920eed5e'
client = TelegramClient('anon', api_id, api_hash)
client.start()

contact_list = {
}

contacts = client(GetContactsRequest(0))
print(contacts)

for u in contacts.users:
     contact_list[u.id] = u.access_hash
     print(contact_list[u.id])


channel ='ASDFZCXV'
channels = {d.entity.username: d.entity
            for d in client.get_dialogs()
            if d.is_channel}
channel = channels[channel]
print(channel)
for u in client.iter_participants(channel, aggressive=True):
  print(u.id, u.first_name, u.last_name, u.username)

current_sentence = ""
banned_word="참외"
error_sentence = "dont say"+banned_word+"please"

@client.on(events.NewMessage)
async def my_event_handler(event):
    chat = await client.get_input_entity('Shit')
    current_sentence = event.raw_text
    print(event.message.to_id.chat_id)
    print(event)
    if event.message.to_id.chat_id == 340126983:
        if banned_word in current_sentence:
            await client.send_message(InputPeerUser(event.message.from_id, contact_list[event.message.from_id]),
                                      error_sentence)


client.run_until_disconnected()


