import json
import dicttoxml
from xml.dom.minidom import parseString
from abc import ABC, abstractmethod


class ConversionData(ABC):
    @abstractmethod
    def write(self, data, filename):
        pass


class JSONConversion(ConversionData):
    def write(self, data, filename):
        with open(filename, 'w') as f:
            f.write(json.dumps(data, indent=2, default=str))


class XMLConversion(ConversionData):
    def write(self, data, filename):
        out = parseString(dicttoxml.dicttoxml(data)).toprettyxml()
        with open(filename, 'w') as f:
            f.write(str(out))