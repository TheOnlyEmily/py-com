# py-com

A module designed to enable a simple form of Reactive Programming, using message passing. 

The MessageHub in message_hub.py is meant for very simple message passing
situations, and has the following limits:

    1. Python's recursion limit: chains of messages can only be as long
       as Python's recursion limit will allow.
    2. Long chains of messages may cause significant slow down, as 
       py-com does not utilize multi tasking of any kind. 
