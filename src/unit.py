# unit.py

class Unit:
    def __init__(self, json_data):
        # Données principales de l'unité
        self.unit_id = json_data.get('unit_id')
        self.wizard_id = json_data.get('wizard_id')
        self.unit_master_id = json_data.get('unit_master_id')
        self.unit_level = json_data.get('unit_level')
        self.stars = json_data.get('class')
        self.attribute = json_data.get('attribute')
        
        # Stats de base (brutes)
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
        
        # Compétences
        self.skills = json_data.get('skills', [])
        
        # Runes
        self.runes = []
        for rune_data in json_data.get('runes', []):
            rune = {
                'slot': rune_data.get('slot_no'),
                'set_id': rune_data.get('set_id'),
                'rank': rune_data.get('rank'),
                'stars': rune_data.get('class'),
                'primary_effect': rune_data.get('pri_eff'),
                'secondary_effects': rune_data.get('sec_eff')
            }
            self.runes.append(rune)
        
        # Artefacts
        self.artifacts = []
        for artifact_data in json_data.get('artifacts', []):
            artifact = {
                'slot': artifact_data.get('slot'),
                'type': artifact_data.get('type'),
                'primary_effect': artifact_data.get('pri_effect'),
                'secondary_effects': artifact_data.get('sec_effects')
            }
            self.artifacts.append(artifact)

    def calculate_hp(self):
        """Calcule les HP totaux selon le niveau et les étoiles"""
        if self._con is None:
            return 0
            
        multiplier = {
            6: 15,  # 6★ = HP base * 15
            5: 14,  # 5★ = HP base * 14
            4: 13,  # 4★ = HP base * 13
            3: 12,  # 3★ = HP base * 12
            2: 11,  # 2★ = HP base * 11
            1: 10   # 1★ = HP base * 10
        }.get(self.stars, 1)
        
        # Le multiplicateur ne s'applique qu'aux monstres niveau 40
        if self.unit_level == 40:
            return self._con * multiplier
        else:
            return self._con