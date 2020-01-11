import requests

class bot(object):
    """ Telegram bot HTTP-request connection object """

    def __init__(self, token):
        self.url = f"https://api.telegram.org/bot{token}/"


    def get_updates(self, offset):
        """Get array of all updates in json"""
        params = {'timeout':60, 'offset':offset, 'allowed_updates':['message']}
        r = requests.get(self.url + "getUpdates", data=params, timeout=60)
        updates = r.json()['result']
        return updates

    def get_latest_update(self, updates):
        """Get latest update"""
        return updates[-1]
        

    def get_chat_id(self, update):
        chat_id = update['message']['chat']['id']
        return chat_id

    def get_latest_text(self, update):
        msg = update['message']['text']
        return msg

    def get_sticker_id(self, update):
        file_id = update['message']['sticker']['file_id']
        return file_id

    def send_message(self, chat_id, msg):
        params = {'chat_id':chat_id, 'text':msg}
        response = requests.post(f"{self.url}sendMessage", data = params)
        return response
    
    def send_sticker(self, chat_id, file_id):
        params = {'chat_id':chat_id, 'sticker':file_id}
        response = requests.post(f"{self.url}sendSticker", data = params)
        return response

    def msg_check(self, update):
        """Check for sticker or text message and returns string based on check"""
        try:
            self.get_latest_text(update)
        except KeyError:

            try:
                self.get_sticker_id(update)
            except KeyError:
                return 'ignore'

            return 'sticker'

        return 'text'

