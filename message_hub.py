class MessageHub:

    def __init__(self, acceptable_messages):
        self._reciever_table = {m:[] for m in acceptable_messages}

    def message_reciever_wrapping(self, other, target_method, messages):
        for m in filter(lambda v: v in self._messages, messages):
            self._reciever_table[m].append(other.target_method)

    def send_message(self, message_name, *message_info):
        recievers = self._reciever_table[message_name]
        full_message = (message_name,) + message_info
        for r in recievers:
            r(*full_message)
