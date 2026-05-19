# Контрольная работа
# Студент: [ваше имя]

# Задача 1. Длина фамилии
def task1():
    name = input("Введите фамилию: ")
    print(f"Моя фамилия {name} имеет длину {len(name)} символов.")


# Задача 2. Умножим строку на число
def task2():
    a_1 = input("Введите первую строку: ")
    a_2 = input("Введите вторую строку: ")
    a_3 = input("Введите третью строку: ")
    print(a_1 * 3 + a_2 * 3 + a_3 * 3)


# Задача 3. Сокращаем до первых букв
def task3():
    a = input("Введите первый город: ")
    b = input("Введите второй город: ")
    c = input("Введите третий город: ")
    print(a[0] + b[0] + c[0])


# Задача 4. Обмен половинок
def task4():
    s = input("Введите строку: ")
    mid = len(s) // 2
    print(s[mid:] + s[:mid])


# Задача 5. Таракан
def task5():
    print("Введите вещи (для выхода нажмите Enter без ввода):")
    while True:
        item = input()
        if item == '':
            break
        if item == 'таракан':
            continue
        print(item)


# Задача 6. Инвентаризация в художественной мастерской
def task6():
    materials = ["Кисть", "Краски", "Разбавитель", "Шпатель", "Холст", "Палитра"]
    year1 = [60, 15, 5, 2, 5, 15]
    year2 = [45, 8, 3, 2, 3, 13]
    year3 = [10, 8, 3, 2, 0, 10]

    print("Способ 1 (без zip):")
    for i in range(len(materials)):
        total = year1[i] + year2[i] + year3[i]
        print(f"Количество приобретенных материалов вида \"{materials[i]}\" за 3 года составило {total} шт.")

    print("\nСпособ 2 (с zip):")
    for material, y1, y2, y3 in zip(materials, year1, year2, year3):
        total = y1 + y2 + y3
        print(f"Количество приобретенных материалов вида \"{material}\" за 3 года составило {total} шт.")


# Задача 7. Сотрудники
def task7():
    workers = {}

    def add_worker(name, position, salary):
        workers[name] = {"position": position, "salary": salary}

    print("Введите имя сотрудника:")
    name = input()
    print("Введите должность:")
    position = input()
    print("Введите зарплату:")
    salary = int(input())
    add_worker(name, position, salary)
    print(workers)

    for name, info in workers.items():
        print(f"{name} {{должность: '{info['position']}', зарплата: {info['salary']}}}")

    print("Введите новую должность для Алексея Трегубова:")
    new_position = input()
    print("Введите новую зарплату:")
    new_salary = int(input())

    workers["Алексей Трегубов"] = {"position": new_position, "salary": new_salary}
    print(workers["Алексей Трегубов"])


if __name__ == "__main__":
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()
    task7()