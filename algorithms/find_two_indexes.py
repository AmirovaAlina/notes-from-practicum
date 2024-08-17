# Квадратичная сложность
def find_two_indexes(data, expected_sum):
    # Для первого индекса и первого слагаемого.
    for first_index, first_value in enumerate(data):
        # Для второго индекса и второго слагаемого.
        for second_index, second_value in enumerate(data):
            # Если индексы равны, то есть это один и тот же элемент...
            if first_index == second_index:
                # ...переходим к следующему элементу.
                continue
            # Если сумма значений равна ожидаемому результату...
            if first_value + second_value == expected_sum:
                # ...вернуть индексы элементов.
                return first_index, second_index


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 11]
    expected_sum = 10
    print(find_two_indexes(data, expected_sum)) 


# Линейная сложность
def find_two_indexes(data, expected_result):
    # В начале работы 
    # - левый указатель указывает на первый элемент списка (с индексом 0):
    left_pointer = 0
    # - правый указатель указывает на последний элемент списка. 
    # Индекс этого элемента на единицу меньше длины списка.
    right_pointer = len(data) - 1
    # Пока индекс левого указателя меньше индекса правого указателя.
    while left_pointer < right_pointer:
        # Считаем сумму двух элементов.
        result = data[left_pointer] + data[right_pointer]       
        # Если она совпадает с искомой...
        if result == expected_result:
            return left_pointer, right_pointer
            # ...возвращаем ответ:
            ...
        # Если сумма больше искомой, то...
        if result > expected_result:
            # ...надо уменьшить сумму: уменьшаем значение правого указателя.
            right_pointer -= 1
        # Все остальные варианты относятся к случаям, когда сумма меньше искомой. 
        else:
            # Сумму надо увеличить, для этого увеличиваем значение левого указателя.
            left_pointer += 1


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 11]
    expected_result = 10
    print(find_two_indexes(data, expected_result))
