import json
from datetime import datetime


def display_last_operations():
    """
    Считывает данные из файла
    """
    with open("operations.json", "r", encoding='utf-8') as file:
        data_dict = json.load(file)
        return data_dict


def sort_execute(data_dict):
    """
    Возвращает список успешных операций
    """
    executed_dict = []
    for operation in data_dict:
        if 'state' in operation:
            if operation['state'] == "EXECUTED":
                executed_dict.append(operation)
            else:
                continue
        else:
            continue
    return executed_dict


def sort_on_data_operations(executed_dict):
    """
    Сортирует успешные операции по дате
    """
    for one_date in executed_dict:
        date_string = one_date["date"]
        parsed_date = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S.%f')
        formatted_date = parsed_date.strftime('%d.%m.%y')
        one_date["date"] = formatted_date

    sort_executed_dict = sorted(executed_dict, key=lambda op: datetime.strptime(op["date"], "%d.%m.%y"), reverse=True)
    return sort_executed_dict


def get_last_five_operations(sort_executed_dict):
    """
    Возвращает оследние 5 операций
    """
    return sort_executed_dict[:5]
