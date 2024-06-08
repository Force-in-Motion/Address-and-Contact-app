output_message = {'greeting': 'Приветствую вас!\nВсе данные успешно загружены\nПрограмма готова к работе'
                    }




def color_text() -> None:
    """
    Создает цветной текст
    :return:
    """
    print('\033')
def output_data(message) -> None:
    """
    Выводит сообщение на консоль
    :param message: Сообщение
    :return: None
    """
    print(message)