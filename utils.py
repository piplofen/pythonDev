import csv
import json
import logging as log
# import os

# headersForQue = os.environ.get("HEADERSFORQUEUE")


# open file
def openFile(path: str, type: str = None):
    try:
        with open(f"{path}.{type}", encoding="utf-8") as file:  # !!!!!!!!!!!!!!!!! encoding="utf-8" !!!!!!!!!!!!!!!!!
            if type == "json":
                data = json.load(file)
            elif type == "csv":
                data = csv.reader(file, delimiter=";")
            elif type is None:
                return file

        return data
    except Exception as e:
        print(e)
        return False


# write file
def writeFile(path: str, type: str, param: str, data: object, print1=0):
    try:
        with open(f"{path}.{type}", param) as file:
            if type == "json":
                data = json.dump(data, file, indent=1)
            elif type == "csv":
                data = csv.writer(file)  # ?
        if print1 == 1:
            print(f"Файл {path}.{type} записан успешно")
    except FileNotFoundError as e:
        print("Файл не найден")


# init logger
def logStart(filePath: str):
    return log.basicConfig(level="INFO", encoding="utf-8", filename=filePath,
                           filemode="a",
                           format="[%(asctime)s] - [%(levelname)s] - [%(filename)s.%(funcName)s(%("
                                  "lineno)d)] > [%(message)s]")

