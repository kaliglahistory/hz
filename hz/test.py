with open('HEALTHIS.txt', 'r') as file:
    lines = file.readlines()

# Редактирование строк
new_lines = []
for line in lines:
    line = line.strip()
    if line.endswith('"'):
        line = '' + line + ''
        new_lines.append(line)
    else:
        new_lines.append(line)

# Создание нового файла с отредактированными строками
with open('output.txt', 'w') as file:
    for line in new_lines:
        file.write(line + '\n')