from src.operations_for_test import operation_list
from src.utils import display_last_operations, sort_execute


testing_list = operation_list


def test_display_last_operations():
    assert testing_list == display_last_operations()


def test_sort_execute(testing_list):
    id_list = []
    state_list = []
    for one in testing_list:
        if "id" in one:
            id_list.append(one["id"])
        if 'state' in one:
            if one['state'] == "EXECUTED":
                state_list.append(one)
            else:
                continue
        else:
            continue

    assert sort_execute(id_list) == []
    assert sort_execute(testing_list) == state_list
