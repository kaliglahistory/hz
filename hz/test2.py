import re

# Функция для преобразования строки
def transform_string(s):
    # Проверяем, есть ли в строке сегмент в закрытых кавычках
    if re.search(r'"[^"]+"', s):
        # Удваиваем все кавычки внутри строки и добавляем кавычки в начало и конец строки
        return '"' + s.replace('"', '""') + '"'
    else:
        # Если закрытых кавычек нет, возвращаем строку без изменений
        return s

# Чтение исходного файла и преобразование строк
with open('HEALTHIS.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    transformed_lines = [transform_string(line.strip()) for line in lines]

# Запись преобразованных строк в новый файл
with open('transformed_file.txt', 'w', encoding='utf-8') as file:
    for line in transformed_lines:
        file.write(line + '\n')

print("Строки были преобразованы и сохранены в 'transformed_file.txt'")
