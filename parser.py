from telethon import TelegramClient, sync


api_id = None
api_hash = ''

file_me = open('messages_me.txt', 'w')
file_di = open('messages_di.txt', 'w')
file_together = open('messages.txt', 'w')


with TelegramClient('new', api_id, api_hash) as client:
    total = 1
    me_counter = 1
    di_counter = 1
    for message in client.iter_messages(304926676):
        if message is None or message.message is None or message.message == '':
            continue
        txt = message.message + '\n'
        file_together.write(txt)
        if message.from_id is not None:
            me_counter += 1
            txt = message.message + '\n'
            file_me.write(txt)
        else:
            di_counter += 1
            txt = message.message + '\n'
            file_di.write(txt)
        # print(total)
        total += 1
    file_together.write(f'total count is {total}')
    file_me.write(f'total count is {me_counter}')
    file_di.write(f'total count is {di_counter}')

file_together.close(), file_di.close(), file_me.close()
