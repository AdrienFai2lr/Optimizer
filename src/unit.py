# src/models/unit.py
from game_data import GameData

class Unit:
    def __init__(self, json_data):
        # Données principales
        self.unit_id = json_data.get('unit_id')
        self.wizard_id = json_data.get('wizard_id')
        self.unit_master_id = json_data.get('unit_master_id')
        self.unit_level = json_data.get('unit_level')
        self.stars = json_data.get('class')
        
        # Utilisation de GameData
        monster_data = GameData.get_monster(self.unit_master_id)
        self.name = monster_data['name']
        self.element = monster_data['element']
        self.type = monster_data['type']
        self.family = monster_data['family']
        self.attribute = GameData.get_monster_attribute(json_data.get('attribute'))
        
        # Stats de base
        self._con = json_data.get('con')
        self._atk = json_data.get('atk')
        self._def = json_data.get('def')
        
        # Stats calculées
        self.stats = {
            'hp': self.calculate_hp(),
            'hp_base': self._con,
            'atk': self._atk,
            'def': self._def,
            'spd': json_data.get('spd'),
            'resist': json_data.get('resist'),
            'accuracy': json_data.get('accuracy'),
            'critical_rate': json_data.get('critical_rate'),
            'critical_damage': json_data.get('critical_damage')
        }
        
        # Skills
        self.skills = json_data.get('skills', [])
        
        # Runes
        self.runes = []
        for rune_data in json_data.get('runes', []):
            if isinstance(rune_data, dict):
                set_data = GameData.get_rune_set(rune_data.get('set_id'))
                quality_data = GameData.get_rune_quality(rune_data.get('rank'))
                rune = {
                    'slot': rune_data.get('slot_no'),
                    'set_id': rune_data.get('set_id'),
                    'set_name': set_data['name'],
                    'set_effect': set_data['effect'],
                    'set_pieces': set_data['pieces'],
                    'rank': rune_data.get('rank'),
                    'rank_name': quality_data['name'],
                    'rank_color': quality_data['color'],
                    'stars': rune_data.get('class'),
                    'level': rune_data.get('upgrade_curr', 0),
                    'primary_effect': self._format_rune_effect(rune_data.get('pri_eff')),
                    'prefix_effect': self._format_rune_effect(rune_data.get('prefix_eff')),
                    'secondary_effects': [
                        self._format_rune_effect(eff) for eff in rune_data.get('sec_eff', [])
                    ]
                }
                if all(v is not None for v in rune.values()):
                    self.runes.append(rune)
        
        # Artefacts
        self.artifacts = []
        for artifact_data in json_data.get('artifacts', []):
            if isinstance(artifact_data, dict):
                type_data = GameData.get_artifact_type(artifact_data.get('type'))
                artifact = {
                    'slot': artifact_data.get('slot'),
                    'type': artifact_data.get('type'),
                    'type_name': type_data['name'],
                    'primary_effect': self._format_artifact_effect(
                        artifact_data.get('pri_effect'),
                        artifact_data.get('type')
                    ),
                    'secondary_effects': [
                        self._format_artifact_effect(eff, artifact_data.get('type'))
                        for eff in artifact_data.get('sec_effects', [])
                    ]
                }
                if all(v is not None for v in artifact.values()):
                    self.artifacts.append(artifact)

    def calculate_hp(self):
        if not isinstance(self._con, (int, float)) or not isinstance(self.stars, int):
            return 0
            
        multiplier = {
            6: 15,
            5: 14,
            4: 13,
            3: 12,
            2: 11,
            1: 10
        }.get(self.stars, 1)
        
        return self._con * multiplier if self.unit_level == 40 else self._con

    def _format_rune_effect(self, effect):
        if not effect or len(effect) < 2:
            return None
            
        stat_id = effect[0]
        value = effect[1]
        stat_data = GameData.get_rune_stat(stat_id)
        
        return {
            'stat': stat_data['name'],
            'value': value,
            'max_value': stat_data['max_value'],
            'grindable': stat_data['grindable']
        }

    def _format_artifact_effect(self, effect, type_id):
        if not effect or len(effect) < 2:
            return None
            
        stat_id = effect[0]
        value = effect[1]
        type_data = GameData.get_artifact_type(type_id)
        stat_data = type_data['stats'].get(stat_id, {'name': 'Unknown', 'max_value': 0})
        
        return {
            'stat': stat_data['name'],
            'value': value,
            'max_value': stat_data['max_value']
        }