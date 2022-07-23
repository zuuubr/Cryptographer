from cryptography.fernet import Fernet
import os
import tkinter


def load_key(patch_to_key):

    # Загрузим имеющийся ключ и вернем в программу
    with open(patch_to_key, "rb") as key_file:
        return key_file.read()

# Функций расшифровки файла
def disencrypt(patch, key, walk):

    if walk is True:
        list = os.listdir(patch)

        for file_name in list:

            if os.path.isfile(patch + '\\' + file_name):
                disencrypt(patch + '\\' + file_name, key, False)
            else:
                disencrypt(patch + '\\' + file_name, key, True)
    else:
        fer = Fernet(key)

        # Прочитаем данные из зашифрованного файла
        with open(patch, "rb") as file:
            data_file = file.read()

        # Расшифровываем данные
        disencrypted_data = fer.decrypt(data_file)

        # Записываем расшиврованные данные назад в файл
        with open(patch, "wb") as file:
            file.write(disencrypted_data)


def main():

    adress = "C:\Программирование\Python\Шифровальщик\Проверка шифровальщика"
    adress_to_key = "key.txt"

    if os.path.isfile(adress) is True:
      walk = False
    else:
      walk = True

    key = load_key(adress_to_key)
    disencrypt(adress, key, walk)

main()
