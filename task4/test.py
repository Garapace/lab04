def common_elements_count(lists):
    if not lists:
        return 0

    common_list = set(lists[0])
    for LIST in lists[1:]:
        common_list &= set(LIST)

    return len(common_list)

def test():
    test_cases = [
        {
            'input': [[1, 2, 3], [2, 3, 4], [2, 5, 6]],
            'expected': 1,  # Общий элемент: 2
        },
        {
            'input': [[1, 1, 1], [1, 1], [1]],
            'expected': 1,  # Общий элемент: 1
        },
        {
            'input': [[1, 2], [3, 4], [5, 6]],
            'expected': 0,  # Общих элементов нет
        },
        {
            'input': [[10, 20, 30], [20, 30, 40], [30, 50, 60]],
            'expected': 1,  # Общий элемент: 30
        },
        {
            'input': [[1, 2, 3]],
            'expected': 3,  # Все элементы уникальны в одном списке
        },
        {
            'input': [[], [1, 2], [3, 4]],
            'expected': 0,  # Один список пустой
        },
        {
            'input': [],
            'expected': 0,  # Пустой ввод
        }
    ]

    for i, test_case in enumerate(test_cases):
        result = common_elements_count(test_case['input'])
        if result == test_case['expected']:
            print(f"Тест {i + 1} прошел успешно!")
        else:
            print(f"Тест {i + 1} провален: ожидаемый результат {test_case['expected']}, полученный результат {result}")

test()