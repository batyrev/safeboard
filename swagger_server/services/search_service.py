import os
import time #
import fnmatch

from swagger_server.config import PATH
from swagger_server.services.db_service import add_new_path, set_status_by_search_id


def find_files_by_mask(search_id, mask):
    """
    Функция ищет файлы в указанной папке по заданному шаблону.
    :param path: str, путь к папке
    :param mask: str, шаблон для поиска файлов
    :return: list, список файлов, соответствующих заданному шаблону
    """
    path = PATH
    files = []
    for root, _, filenames in os.walk(path):
        for filename in fnmatch.filter(filenames, mask):
            files.append(os.path.join(root, filename))
    for file in files:
        add_new_path(search_id, file)
    set_status_by_search_id(search_id, True)
    time.sleep(5) #
    print("ок") #
