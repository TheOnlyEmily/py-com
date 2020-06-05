from context import py_com
from py_com.message_hub import MessageHub


calc_hub = MessageHub(["INPUT", "ANSWER", "ERROR"])

def get_input():
    input_equation = input("Enter equation: ")
    MessageHub.get_instance().send_message("INPUT", input_equation)

def eval_result(message, equation):
    m_hub = MessageHub.get_instance()
    try:
        result = eval(equation)
        m_hub.send_message("ANSWER", result)
    except SyntaxError:
        m_hub.send_message("ERROR", equation)

def display_answer(message, answer):
    print("The answer is: ", answer)

def display_error(message, equation):
    print("Error! {} is not valid python!".format(equation))

calc_hub.add_reciever(eval_result, "INPUT")
calc_hub.add_reciever(display_answer, "ANSWER")
calc_hub.add_reciever(display_error, "ERROR")

if __name__ == "__main__":
    get_input()
