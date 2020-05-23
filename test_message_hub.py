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

    mr1 = MyReciever()
    mr2 = MyReciever()

    mh.add_reciever(mr1.recieve_method, "HELLO")
    mh.add_reciever(mr2.recieve_method, "GOODBYE")

    assert mr1.status == "waiting"
    assert mr2.status == "waiting"

    mh.send_message("HELLO", "WORLD")

    assert mr1.status == "recieved: HELLO WORLD"
    assert mr2.status == "waiting"

    mh.send_message("GOODBYE", "EVENTS")

    assert mr1.status == "recieved: HELLO WORLD"
    assert mr2.status == "recieved: GOODBYE EVENTS"
