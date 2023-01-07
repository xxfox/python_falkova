"""
Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp
Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект; можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
2. * (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
"""
import yaml
import os
import random


def create_file(path, name):
    os.chdir(path)
    letters = [chr(code) for code in range(ord('a'), ord('z') + 1)]
    content = str(random.sample(letters, random.randint(5, 20)))
    if name not in os.listdir(path):
        with open(name, 'w', encoding='utf-8') as f:
            print(f'Created file: {name}')
            f.write(content.strip('[]'))


def create_folder(path, name):
    if name not in os.listdir():
        os.mkdir(os.path.join(path, name))
        print(f'Created folder: {name}')


def is_file_or_folder(path, name):
    if name.find('.') != -1:
        create_file(path, name)
    else:
        create_folder(path, name)


config = yaml.load_all(open('config.yaml'), Loader=yaml.Loader)
main_path = os.getcwd()

for item in config:
    for key, value in item.items():
        is_file_or_folder(main_path, key)
        child_path = os.path.join(main_path, key)
        for i in value:
            if type(i) == dict:
                for k, v in i.items():
                    is_file_or_folder(child_path, k)
                    is_file_or_folder(os.path.join(child_path, k), v)
            else:
                is_file_or_folder(os.path.join(main_path, key), i)

