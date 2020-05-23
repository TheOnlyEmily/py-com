"""
A module that allows modules in a program to communicate without
requiring that said modules have any explicit dependancies on
eachother.

Example:
    >>> class MyReciever:
    ...     def __init__(self):
    ...         self.status = "waiting"
    ...     def recieve_method(self, message, arg):
    ...         self.status = "recieved: {} {}".format(message, arg)
    ...
    >>> mr1 = MyReciever()
    >>> mr2 = MyReciever()
    >>> mh = MessageHub(["HELLO", "GOODBYE"])
    >>> mh.add_reciever(mr1.recieve_method, "HELLO")
    >>> mh.add_reciever(mr2.recieve_method, "GOODBYE")
    >>> mr1.status
    'waiting'
    >>> mr2.status
    'waiting'
    >>> mh.send_message("HELLO", "WORLD")
    >>> mr1.status
    'recieved: HELLO WORLD'
    >>> mr2.status
    'waiting'
    >>> mh.send_message("GOODBYE", "EVENTS")
    >>> mr1.status
    'recieved: HELLO WORLD'
    >>> mr2.status
    'recieved: GOODBYE EVENTS'
"""


class MessageHub:

    def __init__(self, acceptable_messages):
        """
        Args:
            acceptable_messages (tuple[T] | list[T]): A sequence of acceptable
            messages that can be sent/recieved.
        """
        self._reciever_table = {m:[] for m in acceptable_messages}

    def add_reciever(self, rec_func, message):
        self._reciever_table[message].append(rec_func)

    def send_message(self, message_name, *message_info):
        recievers = self._reciever_table[message_name]
        full_message = (message_name,) + message_info
        for r in recievers:
            r(*full_message)
