from importer import Importer
import json


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        file_name = path.split('/')[-1]
        file_path = file_name.split('.')[-1]

        if file_path != "json":
            raise ValueError("Arquivo inválido")

        with open(path, encoding="utf-8") as file:
            all_products = json.load(file)
            return all_products
