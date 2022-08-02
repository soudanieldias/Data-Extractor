from importers.importer import Importer
from importers.csv_importer import CsvImporter
from importers.json_importer import JsonImporter
from importers.xml_importer import XmlImporter
import pytest
import json


CSV_PATH = './files/csv/addresses.csv'
CSV_MOCK = json.load(open('./tests/mocks/csv_mocks.json'))

print(CSV_PATH)
print(CSV_MOCK)

@pytest.mark.dependency()
def test_validate_csvimporter_is_inheriting_importer():
    assert issubclass(CsvImporter, Importer)

@pytest.mark.dependency()
def test_validate_jsonimporter_is_inheriting_importer():
    assert issubclass(JsonImporter, Importer)

@pytest.mark.dependency()
def test_validate_xmlimporter_is_inheriting_importer():
    assert issubclass(XmlImporter, Importer)


@pytest.mark.dependency()
def test_csv_importer():
    import_data = CsvImporter.import_data(CSV_PATH)
    print(import_data)
    assert import_data == CSV_MOCK
