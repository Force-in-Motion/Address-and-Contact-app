import os

def create_folder() -> None:
    """
    Проверяет наличие папки, если ее нет то создает
    :return: None
    """
    if not os.path.isdir(path):
        os.mkdir(path)



def load_data():
    pass


def save_data():
    pass




path = os.environ.get('LOCALAPPDATA') + r'\Notes User'
path_csv = os.path.expanduser('~') + r'\Desktop'