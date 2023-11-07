import re

from src.utils import display_last_operations, sort_execute, sort_on_data_operations, get_last_five_operations

display_last = display_last_operations()
get_executed = sort_execute(display_last)
data_sort = sort_on_data_operations(get_executed)
last_five_operations = get_last_five_operations(data_sort)


def display_operations(operations):
    for one in operations:
        if "from" in one:
            operation_from = one["from"]
            formatted_from = re.sub(r'(\d{4})(\d{2})(\d{4})(\d{4})', r'\1 \2** **** \3', operation_from)
        if "from" not in one:
            formatted_from = "None"
        if "to" in one:
            operation_to = one["to"]
            formatted_to = re.sub(r'(\d{4})(\d{2})(\d{4})(\d{4})', r'\1 \2** **** \3', operation_to)

        print(one["date"], one["description"])
        print(f"{formatted_from} -> {formatted_to}")
        print(f'{one["operationAmount"]["amount"]}, {one["operationAmount"]["currency"]["name"]}, \n')


display_operations(last_five_operations)
