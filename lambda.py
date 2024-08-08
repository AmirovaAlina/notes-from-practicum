def calc(func, first, second):
    return func(first, second)


# Первый аргумент при вызове calc() - это лямбда-функция с нужным выражением:
print(calc(lambda a, b: a + b, 5, 10))   # Складываем.
print(calc(lambda a, b: a * b, 30, 10))  # Умножаем.
print(calc(lambda a, b: a ** b, 30, 2))  # Возводим в степень. 
