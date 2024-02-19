import json


def check_json_file(file_path):
    try:
        # открывает json файл в режиме чтения
        with open(file_path, 'r') as file:
            # загружает файл
            json.load(file)
        print("JSON file is correct.")
    # если json файл не корректен, исключение
    # перехватывает ошибку и печатает ее в консоль
    except json.JSONDecodeError as error:
        # флаг 'f' (f-string) позволяет встраивать
        # значение переменных в текстовую строку
        print(f"Error in JSON file: {error}")
    except FileNotFoundError:
        # еще один способ вставить переменные в строку
        print("File '{}' can't be found.".format(file_path))

# !!!enter the name of your json file here!!!
check_json_file(input("Enter file name: "))
