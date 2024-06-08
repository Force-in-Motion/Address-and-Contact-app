import save_load as sl
import ctypes
import GUI

def run_program():
    """
    Запускает главный жизненный цикл программы
    :return:
    """
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

    GUI.output_data(GUI.output_message['greeting'])

    sl.load_data()

    book_main_loop()

    contact_main_loop()

    sl.save_data()

    # GUI.output_data(GUI.output_message['off'])



def book_main_loop():
    """
    Запускает основное ядро программы
    :return:
    """
    while True:
        GUI.output_data(GUI.output_message['description'])
        input_data = GUI.input_data()
        if input_data == 'exit':
            return

        elif input_data == '':
            GUI.output_data(GUI.output_message['empty'])


def contact_main_loop():
    """
    Запускает основное ядро программы
    :return:
    """
    while True:
        input_data = GUI.input_data()
        if input_data == 'exit':
            return

        elif input_data == '':
            GUI.output_data(GUI.output_message[''])