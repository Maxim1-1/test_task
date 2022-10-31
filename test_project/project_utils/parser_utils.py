import json
from pathlib import Path

class UtilsParse:
    updir = Path("..")
    @staticmethod
    def parse_config():
        with open((Path("..")/'config/config.json'), "r") as file:
            data = json.load(file)
            return data
    @staticmethod
    def parse_test_data():
        with open((Path("..")/'test_data/test_data.json'), "r") as file:
            data = json.load(file)
            return data