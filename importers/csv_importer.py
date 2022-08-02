from .importer import Importer
# from importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        file_name = path.split('/')[-1]
        file_path = file_name.split('.')[-1]

        if file_path != "csv":
            raise ValueError("Arquivo no formato inválido")

        with open(path, encoding="utf-8") as file:
            csv_file = csv.reader(file, delimiter=",", quotechar='"')
            file_data = []
            header, *data = csv_file
            for line in data:
                file_data.append(dict(zip(header, line)))
            return file_data
