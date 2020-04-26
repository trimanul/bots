import vk_api
from datetime import datetime
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

vk_session = vk_api.VkApi(token='//TOKEN//') #insert your vk bot token

session_api = vk_session.get_api()

longpoll = VkBotLongPoll(vk_session, '//GROUP_ID//') #insert your group id

def main():

    while True:
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                if event.from_user:
                    response = event.obj.text.lower()
                    if response == "hi" or response == "hello":
                        session_api.messages.send(
                            user_id=event.obj.from_id,
                            random_id=event.obj.random_id,
                            message='Hello!',
                            attachment='photo-179351750_456239018'
                        )
                        print(str(datetime.strftime(datetime.now(), "%H:%M:%S")) + ':' + 'Bot said: Hello!')

                elif event.from_chat:
                    response = event.obj.text.lower()
                    if response == "hi" or response == "hello":
                        session_api.messages.send(
                            peer_id=event.obj.peer_id,
                            random_id=event.obj.random_id,
                            message='Hello!',
                        )
                        print(str(datetime.strftime(datetime.now(), "%H:%M:%S")) + ':' + 'Bot said: Hello!')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        quit()

