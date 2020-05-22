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

        def recieve_method(self, message, x):
            return "recieved: {} {}".format(message, x)

    mr1 = MyReciever()
    mr2 = MyReciever()

    mh.add_reciever(mr1.recieve_method, "HOME")

    assert mh._reciever_table["HOME"] == mr1

    mh.add_reciever(mr2.recieve_method, "GOODBYE")

    assert mh._reciever_table["GOODBYE"] == mr2

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
