from message_hub import MessageHub


def test_init():
    POSSIBLE_MESSAGES = ["HELLO", "GOODBYE"]
    mh = MessageHub(POSSIBLE_MESSAGES)

    assert mf._reciever_table == {"HELLO":[], "GOODBYE":[]}

def test_add_reciever():
    POSSIBLE_MESSAGES = ["HELLO", "GOODBYE"]
    mh = MessageHub(POSSIBLE_MESSAGES)

    class MyReciever:

        def __init__(self):
            self.status = "waiting"

        def recieve_method(self, message):
            return "recieved: {}".format(message)

    mr = MyReciever()
