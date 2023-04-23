import os
import time #
import fnmatch
from datetime import datetime

from swagger_server.config import PATH
from swagger_server.services.db_service import add_new_path, set_status_by_search_id


def find_files(search_id,
               mask,
               search_string,
               date_string,
               date_comparison_rule,
               size,
               size_comparison_rule):
    """
    Функция ищет файлы в указанной папке по заданным параметрам.
    :return: list, список файлов, соответствующих заданным параметрам
    """
    path = PATH
    files = []
    for root, _, filenames in os.walk(path):
        for filename in fnmatch.filter(filenames, mask):
            full_filename = os.path.join(root, filename)
            if find_string_in_file(full_filename,
                                   search_string) and \
               compare_file_creation_date(full_filename,
                                          date_string,
                                          date_comparison_rule) and \
               compare_file_size(full_filename,
                                 size,
                                 size_comparison_rule):
                files.append(full_filename)
    for file in files:
        add_new_path(search_id, file)
    time.sleep(5) #
    set_status_by_search_id(search_id, True)
    print("ок") #


def find_string_in_file(filename, search_string):
    encodings = ['utf-8', 'cp1251', 'iso-8859-1']
    for enc in encodings:
        try:
            with open(filename, 'r', encoding=enc) as file:
                for line in file:
                    if search_string in line:
                        return True
                return False
        except UnicodeDecodeError:
            continue
    return False


def compare_file_creation_date(file_name, date_string, comparison_rule):
    """
    Сравнивает дату создания файла с датой, которую мы передаем, используя правило сравнения, которое мы также передаем.
    Возвращает True, если сравнение истинно, в противном случае возвращает False.
    """
    # Получаем время создания файла
    file_creation_time = os.path.getctime(file_name)

    # Проверяем, является ли переданное значение даты допустимым форматом
    try:
        date = datetime.fromisoformat(date_string)
    except ValueError as e:
        raise ValueError(f"Invalid date format: {date_string}.") from e

    # Сравниваем даты, используя переданное правило сравнения
    return comparison(comparison_rule, file_creation_time, date.timestamp())


def compare_file_size(file_name, size, comparison_rule):
    # Получаем размер файла по имени
    file_size = os.path.getsize(file_name)

    # Сравниваем размер, используя переданное правило сравнения
    return comparison(comparison_rule, file_size, size)


def comparison(comparison_rule, arg1, arg2):
    if comparison_rule == "eq":
        return arg1 == arg2
    elif comparison_rule == "gt":
        return arg1 > arg2
    elif comparison_rule == "lt":
        return arg1 < arg2
    elif comparison_rule == "ge":
        return arg1 >= arg2
    elif comparison_rule == "le":
        return arg1 <= arg2
    else:
        raise ValueError(f"Invalid comparison rule: {comparison_rule}.")
