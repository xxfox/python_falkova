"""
Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике). Написать скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
  |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
(они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача,
которая решена, например, во фреймворке django.
"""
import os
import shutil

main_path = r'C:\Users\NewUser\PycharmProjects\lesson 7\my_project'
copy_to = r'C:\Users\NewUser\PycharmProjects\lesson 7\my_project\templates'

for root, dirs, files in os.walk(main_path):
    for dir in dirs:
        if dir == 'templates':
            print("Эту папку скопировать нельзя")
        else:
            shutil.copytree(os.path.join(root, dir), copy_to, dirs_exist_ok=True)
