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