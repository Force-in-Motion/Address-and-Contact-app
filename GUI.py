output_message = {'greeting': """Приветствую вас!
      Все данные успешно загружены
      Программа готова к работе""",
                  'base_input': '\033[34mВведите команду >> ',
                  'empty': 'Пустая строка не может быть принята'
                    }




def color_text_output() -> None:
    """
    Создает цветной текст
    :return:
    """
    print('\033[33mINFO: \033[0m', end='')

def color_text_input() -> None:
    """
    Создает цветной текст
    :return:
    """
    print('\033[35mUSER: \033[0m', end='')


def output_data(message) -> None:
    """
    Выводит сообщение на консоль
    :param message: Сообщение
    :return: None
    """
    color_text_output()
    print(f'\033[34m{message}\n')

def input_data() -> str:
    """
    Пренимает ввод пользователя
    :return: Возвращает строку
    """
    color_text_input()
    return input(output_message['base_input'])

