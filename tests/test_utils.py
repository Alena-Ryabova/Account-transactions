import json
import os

from src.utils import display_last_operations


def test_display_last_operations():
    # Подготовьте файл "operations.json" с тестовыми данными
    test_data = {
        "id": 1,
        "state": "TEST_STATE",
        # Другие поля...
    }

    with open("operations.json", "w", encoding="utf-8") as file:
        json.dump(test_data, file)

    # Вызов функции и проверка результата
    result = display_last_operations()
    assert result == test_data  # Проверьте, что результат соответствует ожидаемым данным

    # Очистите файл после теста (если это необходимо)
    os.remove("operations.json")

if __name__ == '__main__':
    pytest.main()



