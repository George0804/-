# Самостоятельная работа: Кортежи. Создание функций
# Студент: [ваше имя]

# Задача 1. Срез кортежа
def task1():
    baza = (4, 16, 45, 8, 34, 14, 18, 24, 13, 18, 40, 47, 7, 12, 16)
    result = baza[1::2]
    print("Задача 1:", result)
    return result

# Задача 2. Конференция
def task2():
    pack = ('программа конференции', 'блокнот', 'ручка', 'магнитик')
    participants = 20
    result = (pack * (participants // len(pack) + 1))[:participants]
    print("Задача 2:", result)
    return result

# Задача 3. Статистика раскрытых дел
def task3():
    crimes = (24, 37, 49, 83, 12, 46, 54, 93, 27, 13, 39, 42, 69, 39, 96, 12, 40, 33, 50, 30, 29, 32, 81, 60)
    max_crimes = max(crimes)
    min_crimes = min(crimes)
    print("Задача 3:", max_crimes, min_crimes)
    return max_crimes, min_crimes

# Задача 4. Затраты на закупку
def task4():
    def multy(volume, price):
        return volume * price
    print("Задача 4:", multy(10, 100))
    return multy(10, 100)

# Задача 5. Числа Фибоначчи
def task5():
    def fibon(num):
        num1 = 0
        num2 = 1
        if num < 1:
            return 0
        if num == 1:
            return 0
        if num == 2:
            return 1
        for i in range(2, num):
            num1, num2 = num2, num1 + num2
        return num2
    n = int(input("Введите номер числа Фибоначчи: "))
    print("Задача 5:", fibon(n))
    return fibon(n)

# Задача 6. Алгоритм Евклида
def task6():
    def NOD(a, b):
        while a != b:
            if a > b:
                a = a - b
            else:
                b = b - a
        return a
    print("Задача 6:", NOD(32, 24))
    return NOD(32, 24)

# Запуск всех задач
if __name__ == "__main__":
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()