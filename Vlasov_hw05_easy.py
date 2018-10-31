# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


def create_dirs():
    from os import path, getcwd, mkdir
    current_dir = getcwd()
    for i in range(1, 10):
        try:
            dir_name = str("dir_{}".format(i))
            new_dir_pass = path.join(current_dir, dir_name)
            mkdir(new_dir_pass)
            print("Директория {} создана".format(dir_name))
        except FileExistsError:
            print("Директория {} уже существует".format(dir_name))


def delete_dirs():
    from os import path, getcwd, rmdir
    current_dir = getcwd()
    for i in range(1, 10):
        try:
            dir_name = str("dir_{}".format(i))
            new_dir_pass = path.join(current_dir, dir_name)
            rmdir(new_dir_pass)
            print("Директория {} успешно удалена".format(dir_name))
        except OSError:
            print("Директория {} не существует или не пустая! ".format(dir_name))


if __name__ == '__main__':
    create_dirs()
    delete_dirs()

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def get_folders():
    from os import listdir, path
    folders = listdir()
    folders = [item for item in folders if path.isdir(item)]
    print(folders)


if __name__ == '__main__':
    get_folders()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def copy_current_file():
    from os import path
    from shutil import copy2
    curr_file = str(path.basename(__file__))
    idx_ext = curr_file.rfind(".")
    split_name = (curr_file[:idx_ext], curr_file[idx_ext + 1:])
    new_filename = "{}_copy.{}".format(split_name[0], split_name[1])
    try:
        copy2(curr_file, new_filename)
        print("Файл успешно скопирован")
    except IOError:
        print("Невозможно сохранить копию файла в текущую директорию")


if __name__ == '__main__':
    copy_current_file()


# Модификации функций для normal


def create_dir(name):
    from os import path, getcwd, mkdir
    current_dir = getcwd()
    try:
        new_dir_path = path.join(current_dir, name)
        mkdir(new_dir_path)
        print("Директория {} создана".format(name))
    except FileExistsError:
        print("Директория {} уже существует".format(name))


def delete_dir(name):
    from os import path, getcwd, rmdir
    current_dir = getcwd()
    try:
        dir_path = path.join(current_dir, name)
        rmdir(dir_path)
        print("Директория {} успешно удалена".format(name))
    except OSError:
        print("Директория {} не существует или не пустая! ".format(name))