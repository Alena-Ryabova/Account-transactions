from src.operations_for_test import operation_list
from src.utils import display_last_operations, sort_execute, sort_on_data_operations, get_last_five_operations
import pytest

from tests.last_five1 import five_operations


@pytest.fixture
def testing_list():
    return operation_list


@pytest.fixture
def operations_for_test():
    return [{
        "id": 615064591,
        "state": "CANCELED",
        "date": "2019-08-26T10:50:58.294041"
    }, {
        "id": 147815167,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041"
    }]


def test_display_last_operations():
    assert display_last_operations("operations.json")[0] == {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }


def test_sort_execute(operations_for_test):
    assert sort_execute(operations_for_test) == [{
        "id": 147815167,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041"
    }]
    assert sort_execute(operations_for_test[0:1]) == []


def test_sort_on_data_operations(operations_for_test):
    for one in sort_on_data_operations(operations_for_test):
        assert one["date"] == '26.08.19'


def test_get_last_five_operations(testing_list):
    assert get_last_five_operations(testing_list) == five_operations
