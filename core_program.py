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

    start_main_loop()

    sl.save_data()

    # GUI.output_data(GUI.output_message['off'])



def start_main_loop():
    """
    Запускает основное ядро программы
    :return:
    """
    pass