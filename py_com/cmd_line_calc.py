from message_hub import MessageHub


calc_hub = MessageHub(["GET_INPUT", "INPUT", "ANSWER"])

def get_cli_input(message):
    input_equation = input("Enter equation: ")
    calc_hub.send_message("INPUT", input_equation)

def calculate_result(message, equation):
    try:
        result = eval(equation)
    except SyntaxError:
        raise SystemExit
    calc_hub.send_message("ANSWER", result)

def display_answer(message, answer):
    print("The answer is: ", answer)
    input("Press any key to continue.")

calc_hub.add_reciever(get_cli_input, "GET_INPUT")
calc_hub.add_reciever(calculate_result, "INPUT")
calc_hub.add_reciever(display_answer, "ANSWER")

if __name__ == "__main__":
    while True:
        calc_hub.send_message("GET_INPUT")
