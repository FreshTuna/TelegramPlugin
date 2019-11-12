# TelegramPlugin
Plugin for Telegram

Telethon Basics
-------------------

```python
from telethon import TelegramClient, events, sync

client = TelegramClient('session_name', api_id, api_hash)
client.start(phone_number)

client.send_message('jangjunyoung','Hello!')

messages = client.get_messages('jangjunyoung')
print(messages[0].message)

```

You should not make your file name as 'telethon.py'

username is set at none if you just made your account. Go to setting and set your username


Telethon Contacts
--------------------

```python
contacts = client(GetContactsRequest(0))
print(contacts)

for u in contacts.users:
    client.send_message(InputPeerUser(u.id, u.access_hash),"hi")
```
Import these:
```python
  from telethon.tl.functions.contacts import GetContactsRequest
  from telethon.tl.types import InputPeerUser
```
For the output it sends messages to your contact list.


```python
invite_link = 'http://t.me//AS##sDFX'
user_input_channel = invite_link

if user_input_channel.isdigit():
    entity = PeerChannel(int(user_input_channel))
else:
    entity = user_input_channel

my_channel = client.get_entity(invite_link)
```

Telethon Get Message from Channel
--------------------------------
```python
my_channel = client.get_entity(invite_link) #invite_link was declared above
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
    hash=0))

for message in posts.messages:
    print(message.message)
```

This code shows all the message inside the channel.
