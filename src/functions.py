import json
import re


def load_json(file_name, encoding='utf-8'):
    """Загрузка формата json из выбранного файла"""
    with open(file_name, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def true_date(dict_):
    """Обработка строки с датой и вывод даты с описанием перевода"""
    date = dict_["date"]
    list_ = re.split("[T-]", date)
    result = ".".join(list_[2::-1]) + " " + dict_["description"]
    return result


def card_and_bank_account(dict_):
    """Обработка данных карты и счета"""
    if dict_.get("from") == None:
        from_ = "Данные отправителя не определены"
        to = dict_["to"][:-5:-1] + "**"
        data = f"{from_} -> {to[::-1]}"
        return data
    else:
        from_ = dict_["from"].split()
        name_card = from_[0]
        number_card = from_[1][:6] + "******" + from_[1][-4:]
        number_card_true = ' '.join(number_card[i*4:(i+1)*4] for i in range(4))
        to = dict_["to"][:-5:-1] + "**"
        name_to = dict_["to"].split()[0]
        data = f"{name_card} {number_card_true} -> {name_to} {to[::-1]}"
        return data
