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
        Creates a new message hub, by specifying a list of valid
        message types.

        Args:
            acceptable_messages (tuple[T] | list[T]): A sequence of acceptable
            messages that can be sent/recieved.
        """
        self._reciever_table = {m:[] for m in acceptable_messages}
        
    def add_reciever(self, rec_func, message):
        """
        Adds a function that can recieve a type of message.

        Args:
            rec_func (function | method): The function that the message and
            its contents will be passed to.
            message (T): The message type that the rec_func recieves.

        Raises:
            KeyError: If message is not in the reciever_table, and is
            not a valid message type.
        """
        self._reciever_table[message].append(rec_func)

    def send_message(self, message, *message_info):
        """
        Sends a message and the info it comes with, to the function(s)
        or method(s) that are meant to recieve them.

        Args:
            message (T): The message that will contain message_into.
            message_info (tuple[T]): Optional, additional info that
            will be passed with the message.

        Raises:
            KeyError: When message is not a valid message type.
            TypeError: When the length message, combined with the
            message_info, is greater than the number of arguments the
            function/method recieveing them can accomidate.
            RecursionError: If a message passing chain gets too long.
        """
        recievers = self._reciever_table[message]
        full_message = (message,) + message_info
        for r in recievers:
            r(*full_message)
