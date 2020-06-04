import re

from context import py_com
from py_com.message_hub import MessageHub


calc_hub = MessageHub(["CHECK", "ERROR", "VALID", "ANSWER"])

def get_input():
    equation = input("Enter simple equation: ")
    calc_hub.send_message("CHECK", equation)

def check_input(message, equation):
    re_prog = re.compile(r"[0-9]+ *[\+|\-|\*|\/] *[0-9]+")
    if re_prog.match(equation):
        calc_hub.send_message("VALID", equation)
    else:
        calc_hub.send_message("ERROR", equation)

def process_equation(message, equation):
    answer = eval(equation)
    calc_hub.send_message("ANSWER", answer)

def display_error(message, equation):
    print("Error! {} is not a simple equation!".format(equation))

def display_answer(message, answer):
    print("The answer is: ", answer)

calc_hub.add_reciever(check_input, "CHECK")
calc_hub.add_reciever(process_equation, "VALID")
calc_hub.add_reciever(display_error, "ERROR")
calc_hub.add_reciever(display_answer, "ANSWER")

if __name__ == "__main__":
    get_input()
