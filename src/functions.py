import json


def load_json(file_name, encoding='utf-8'):
    """Загрузка формата json из выбранного файла"""
    with open(file_name, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data
