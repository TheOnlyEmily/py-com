class MessageHub:

    def __init__(self, acceptable_messages):
        self._reciever_table = {m:[] for m in acceptable_messages}

    def add_reciever(self, rec_func, message):
        self._reciever_table[message].append(rec_func)

    def send_message(self, message_name, *message_info):
        recievers = self._reciever_table[message_name]
        full_message = (message_name,) + message_info
        for r in recievers:
            r(*full_message)
