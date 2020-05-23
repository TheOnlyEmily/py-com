from message_hub import MessageHub


def test_init():
    POSSIBLE_MESSAGES = ["HELLO", "GOODBYE"]
    mh = MessageHub(POSSIBLE_MESSAGES)

    assert mh._reciever_table == {"HELLO":[], "GOODBYE":[]}

def test_send_message():
    POSSIBLE_MESSAGES = ["HELLO", "GOODBYE"]
    mh = MessageHub(POSSIBLE_MESSAGES)

    class MyReciever:

        def __init__(self):
            self.status = "waiting"

        def recieve_method(self, message, x):
            self.status = "recieved: {} {}".format(message, x)

    mr = MyReciever()

    mh.add_reciever(mr.recieve_method, "HELLO")

    assert mr.status == "waiting"

    mh.send_message("HELLO", "WORLD")

    assert mr.status == "recieved: HELLO WORLD"
