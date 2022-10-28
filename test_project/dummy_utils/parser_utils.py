import json


class UtilsParse:
    @staticmethod
    def parse_config():
        with open(r'..\config\config.json', "r") as file:
            data = json.load(file)
            return data

    @staticmethod
    def write_config(data):
        with open(r'..\config\config.json', "w") as file:
            json.dump(data, file)