import requests
from bot_class import *

def main():
    tgbot = Bot("//TOKEN//") #insert your Telegram bot token
    new_offset = None
    
    while True:
        
        updates = tgbot.get_updates(new_offset)
        if updates != []:
            update = tgbot.get_latest_update(updates)
            chat_id = tgbot.get_chat_id(update)
            update_id = update['update_id']

            check = tgbot.msg_check(update)

            if check == 'text':
                text = tgbot.get_latest_text(update)
                tgbot.send_message(chat_id, text)
                print("New message: " + text)

            elif check == 'sticker':
                file_id = tgbot.get_sticker_id(update)
                tgbot.send_sticker(chat_id, file_id)
                print("New sticker")

            elif check == 'ignore':
                print("Something not interesting")
        
            new_offset = update_id + 1
        else:
            continue

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        quit()









