from functions import *

file_name = "operations.json"

if __name__ == '__main__':
    data = load_json(file_name)
    count = 0
    for dict_ in reversed(data):
        if count == 5:
            break
        if dict_.get("state") == None:
            continue
        if dict_["state"] == "EXECUTED":
            print(true_date(dict_), card_and_bank_account(dict_), money(dict_), sep="\n", end="\n\n")
            count += 1
        