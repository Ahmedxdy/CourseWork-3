from functions import *

file_name = "operations.json"

if __name__ == '__main__':
    data = load_json(file_name)
    for i in data:
        print(i["id"])