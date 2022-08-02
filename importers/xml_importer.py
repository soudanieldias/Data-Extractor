from .importer import Importer
import xmltodict


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        file_name = path.split('/')[-1]
        file_path = file_name.split('.')[-1]

        if file_path != "xml":
            raise ValueError("Arquivo no formato inválido")

        with open(path, encoding="utf-8") as file:
            all_data = xmltodict.parse(file.read())

            return all_data["dataset"]["record"]