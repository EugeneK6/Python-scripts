# библиотека которая позволяет взаимодействовать
# с файловой систем оп
import os
import json


def check_json_files(folder_path):
    # цикл который проходит по всем файлам в папке с помощью os.listdir
    for filename in os.listdir(folder_path):
        # проверяет что бы перебераемый файл имел окончание .json
        if filename.endswith('.json'):
            # создает полный путь для каждого выбраного
            # файла из пути к папке и имени файла
            file_path = os.path.join(folder_path, filename)
            try:
                with open(file_path, 'r') as file:
                    json.load(file)
                print(f"JSON file '{filename}' is correct.")
            except json.JSONDecodeError as error:
                print(f"Error in JSON file '{filename}': {error}")

# check_json_files("E:/projects/homework/jsonfold")
check_json_files(input("Enter the full path: "))
