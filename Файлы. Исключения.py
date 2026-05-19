# Самостоятельная работа: Файлы. Исключения
# Студент: [Мамиконян Георгий ДПИ25-1с]

import os
import random
import re
import string


# Создание тестовых файлов, если их нет
def create_test_files():
    # Создаем input.txt для задач 2, 4, 5
    if not os.path.exists('input.txt'):
        with open('input.txt', 'w', encoding='utf-8') as f:
            f.write("Привет мир. Как дела? Это тестовый файл! В нем есть предложения.")

    # Создаем russian_text.txt для задачи 3
    if not os.path.exists('russian_text.txt'):
        with open('russian_text.txt', 'w', encoding='utf-8') as f:
            f.write("Привет! Это русский текст для транслитерации. Нужно преобразовать его в латиницу.")


# Задача 1. Размер папки
def task1():
    def get_folder_size(folder_path):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(folder_path):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                try:
                    total_size += os.path.getsize(file_path)
                except OSError:
                    continue
        return total_size

    size = get_folder_size(".")
    print("Задача 1:", size, "байт")
    return size


# Задача 2. Перемешивание слов в предложениях
def task2():
    def shuffle_words_in_sentences(input_file, output_file):
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                text = f.read()
        except FileNotFoundError:
            print(f"Файл {input_file} не найден")
            return

        sentences = re.split(r'([.!?])', text)
        result = []

        for i in range(0, len(sentences), 2):
            sentence = sentences[i]
            punct = sentences[i + 1] if i + 1 < len(sentences) else ''
            words = sentence.split()
            if words:
                random.shuffle(words)
                result.append(' '.join(words) + punct)
            else:
                result.append(punct)

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(''.join(result))

    shuffle_words_in_sentences('input.txt', 'output_shuffled.txt')
    print("Задача 2: выполнено (файл output_shuffled.txt)")


# Задача 3. Транслитерация
def task3():
    def translit(text):
        mapping = {
            'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo',
            'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm',
            'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
            'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
            'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya',
            'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'Yo',
            'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M',
            'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
            'Ф': 'F', 'Х': 'Kh', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch',
            'Ъ': '', 'Ы': 'Y', 'Ь': '', 'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya'
        }
        result = ''
        for ch in text:
            result += mapping.get(ch, ch)
        return result

    def convert_to_translit(input_file, output_file):
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                text = f.read()
        except FileNotFoundError:
            print(f"Файл {input_file} не найден")
            return

        translit_text = translit(text)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(translit_text)

    convert_to_translit('russian_text.txt', 'translit_output.txt')
    print("Задача 3: выполнено (файл translit_output.txt)")


# Задача 4. Подсчет букв в файле
def task4():
    def count_letters(input_file):
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                text = f.read()
        except FileNotFoundError:
            print(f"Файл {input_file} не найден")
            return 0

        letter_count = 0
        for ch in text:
            if ch.isalpha():
                letter_count += 1
        return letter_count

    result = count_letters('input.txt')
    print("Задача 4:", result, "букв")
    return result


# Задача 5. Подсчет букв (альтернативный вариант)
def task5():
    def count_letters_v2(input_file):
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                text = f.read()
        except FileNotFoundError:
            print(f"Файл {input_file} не найден")
            return 0

        letters = string.ascii_letters + 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        letter_count = sum(1 for ch in text if ch in letters)
        return letter_count

    result = count_letters_v2('input.txt')
    print("Задача 5:", result, "букв")
    return result


# Задача 6. Обработка ввода
def task6():
    value1 = input("Первое значение: ")
    value2 = input("Второе значение: ")

    try:
        num1 = float(value1)
        num2 = float(value2)
        result = num1 + num2
        print("Результат:", result)
    except ValueError:
        result = str(value1) + str(value2)
        print("Результат:", result)


# Запуск всех задач
if __name__ == "__main__":
    create_test_files()
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()