import json
import re


def load_json(file_name, encoding='utf-8'):
    """Загрузка формата json из выбранного файла"""
    with open(file_name, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def true_date(dict_):
    """Обработка строки с датой"""
    date = dict_["date"]
    list_ = re.split("[T-]", date)
    result = ".".join(list_[2::-1])
    return result


# def reversed_executed_data(data):
#     """Обработка данных клиента в обратном порядке и получение словаря с успешными операциями"""
#     pass
