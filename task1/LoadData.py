import json
from abc import ABC, abstractmethod


class LoadDATA(ABC):
    @abstractmethod
    def load(self, filename):
        pass


class LoadJSON(LoadDATA):
    def load(self, filename):
        with open(filename, 'r') as f:
            json_data = json.load(f)
            return json_data
