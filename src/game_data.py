# game_data.py

from unit import Unit  # Vérifie que l'importation est correcte

class GameData:
    def __init__(self, unit):
        self.unit = unit
    
    @classmethod
    def from_json(cls, json_data):
        unit = Unit.from_json(json_data)
        return cls(unit)
