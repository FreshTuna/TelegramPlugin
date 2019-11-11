from telethon import TelegramClient, events, sync

api_id = 4####0
api_hash = '#####42c1ace1#####ca1e1d920eed5e'
phone_number = 'phonenumber'
client = TelegramClient('session_name', api_id, api_hash)
client.start(phone_number)

client.send_message('jangjunyoung','Hello!')

messages = client.get_messages('jangjunyoung')
print(messages[0].message)