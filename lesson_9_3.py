"""
Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница
размера файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках),
размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
"""
import json
import os

main_path = r'my_project\templates'
all_files = list((item for item in os.scandir(main_path)))
keys = (10, 50, 100)
info_dict = {}

for key in keys:
    count = 0
    extension = []
    for file in all_files[:]:
        if os.stat(file).st_size < key:
            extension.append(((file.name).split('.'))[-1])
            count += 1
            if file.name in extension:
                all_files.remove(file)
    info_dict[key] = (count, list(set(extension)))
print(info_dict)

with open('extension.json', 'w') as f:
    json.dump(info_dict, f)
