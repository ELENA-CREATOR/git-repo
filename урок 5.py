import os
import shutil
import sys

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def list_dir(main_path):
    for _ in os.listdir(main_path):
        print(_)
main_path = os.getcwd()

list_dir(main_path)


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
try:
    for i in range(1, 10):
        os.mkdir("dir_" + str(i))
except:
    print("Уже создан")
a = input("введите ")
print(a)
try:
    for i in range(1, 10):
        os.rmdir("dir_" + str(i))
except:
    print("уже удален")


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def current_file_copy ():
    name_file = os.path.realpath(__file__)
    new_file = name_file +'.copy'
    if os.path.isfile(new_file) != True:
        shutil.copy(name_file, new_file)
        return new_file + ' - создан'
    else:
        return 'Файл уже скопирован'

if __name__ == '__main__':
    print(current_file_copy())
