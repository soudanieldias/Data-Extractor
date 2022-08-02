from importers.csv_importer import CsvImporter
from importers.json_importer import JsonImporter
from importers.xml_importer import XmlImporter


class Extractor():
    @staticmethod
    def file_switch(path):
        file_name = path.split('/')[-1]
        file_extension = file_name.split('.')[-1]

        import_from = {
          "csv": CsvImporter.import_data,
          "json": JsonImporter.import_data,
          "xml": XmlImporter.import_data
        }

        return import_from[file_extension]
