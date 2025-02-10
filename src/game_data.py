# src/data/game_data.py

class GameData:
    MONSTERS = {
        14011: {'name': 'Sigmarus', 'element': 'Water', 'type': 'Attack', 'stars': 5, 'family': 'Phoenix'},
        14012: {'name': 'Perna', 'element': 'Fire', 'type': 'Attack', 'stars': 5, 'family': 'Phoenix'},
        14013: {'name': 'Teshar', 'element': 'Wind', 'type': 'Attack', 'stars': 5, 'family': 'Phoenix'},
        15011: {'name': 'Veromos', 'element': 'Dark', 'type': 'Support', 'stars': 5, 'family': 'Ifrit'},
        15012: {'name': 'Theomars', 'element': 'Water', 'type': 'Attack', 'stars': 5, 'family': 'Ifrit'},
        15013: {'name': 'Tesarion', 'element': 'Fire', 'type': 'Support', 'stars': 5, 'family': 'Ifrit'},
        15014: {'name': 'Akhamamir', 'element': 'Wind', 'type': 'Attack', 'stars': 5, 'family': 'Ifrit'},
        15015: {'name': 'Elsharion', 'element': 'Light', 'type': 'Attack', 'stars': 5, 'family': 'Ifrit'},
        16011: {'name': 'Camilla', 'element': 'Water', 'type': 'HP', 'stars': 5, 'family': 'Valkyrie'},
        16012: {'name': 'Vanessa', 'element': 'Fire', 'type': 'Support', 'stars': 5, 'family': 'Valkyrie'},
        16013: {'name': 'Katarina', 'element': 'Wind', 'type': 'Attack', 'stars': 5, 'family': 'Valkyrie'},
        16014: {'name': 'Trinity', 'element': 'Dark', 'type': 'Attack', 'stars': 5, 'family': 'Valkyrie'},
        16015: {'name': 'Akroma', 'element': 'Light', 'type': 'Defense', 'stars': 5, 'family': 'Valkyrie'}
    }
    
    RUNE_SETS = {
        1: {'name': 'Energy', 'pieces': 2, 'effect': 'HP +15%'},
        2: {'name': 'Guard', 'pieces': 2, 'effect': 'Defense +15%'},
        3: {'name': 'Swift', 'pieces': 4, 'effect': 'Speed +25%'},
        4: {'name': 'Blade', 'pieces': 2, 'effect': 'Critical Rate +12%'},
        5: {'name': 'Rage', 'pieces': 4, 'effect': 'Critical Damage +40%'},
        6: {'name': 'Focus', 'pieces': 2, 'effect': 'Accuracy +20%'},
        7: {'name': 'Endure', 'pieces': 2, 'effect': 'Resistance +20%'},
        8: {'name': 'Fatal', 'pieces': 4, 'effect': 'Attack Power +35%'},
        10: {'name': 'Despair', 'pieces': 4, 'effect': '25% chance to stun'},
        11: {'name': 'Vampire', 'pieces': 4, 'effect': '35% life steal'},
        13: {'name': 'Violent', 'pieces': 4, 'effect': '22% chance for extra turn'},
        14: {'name': 'Nemesis', 'pieces': 2, 'effect': 'ATB +4% when hit'},
        15: {'name': 'Will', 'pieces': 2, 'effect': 'Immunity for 1 turn'},
        16: {'name': 'Shield', 'pieces': 2, 'effect': 'Shield 15% of HP'},
        17: {'name': 'Revenge', 'pieces': 2, 'effect': '15% counter chance'},
        18: {'name': 'Destroy', 'pieces': 2, 'effect': 'Reduce enemy max HP'},
        19: {'name': 'Fight', 'pieces': 2, 'effect': 'Team ATK +8%'},
        20: {'name': 'Determination', 'pieces': 2, 'effect': 'Team DEF +8%'},
        21: {'name': 'Enhance', 'pieces': 2, 'effect': 'Team HP +8%'},
        22: {'name': 'Accuracy', 'pieces': 2, 'effect': 'Team ACC +10%'},
        23: {'name': 'Tolerance', 'pieces': 2, 'effect': 'Team RES +10%'}
    }
    
    RUNE_QUALITY = {
        1: {'name': 'Normal', 'color': 'white'},
        2: {'name': 'Magic', 'color': 'green'},
        3: {'name': 'Rare', 'color': 'blue'},
        4: {'name': 'Hero', 'color': 'purple'},
        5: {'name': 'Legend', 'color': 'orange'}
    }
    
    RUNE_STATS = {
        1: {'name': 'HP flat', 'max_value': 375, 'grindable': True},
        2: {'name': 'HP%', 'max_value': 8, 'grindable': True},
        3: {'name': 'ATK flat', 'max_value': 20, 'grindable': True},
        4: {'name': 'ATK%', 'max_value': 8, 'grindable': True},
        5: {'name': 'DEF flat', 'max_value': 20, 'grindable': True},
        6: {'name': 'DEF%', 'max_value': 8, 'grindable': True},
        8: {'name': 'SPD', 'max_value': 6, 'grindable': True},
        9: {'name': 'CRIT Rate%', 'max_value': 6, 'grindable': False},
        10: {'name': 'CRIT DMG%', 'max_value': 7, 'grindable': False},
        11: {'name': 'Resistance%', 'max_value': 8, 'grindable': True},
        12: {'name': 'Accuracy%', 'max_value': 8, 'grindable': True}
    }
    
    ARTIFACT_TYPES = {
        1: {
            'name': 'Attribute',
            'elements': ['Fire', 'Water', 'Wind'],
            'stats': {
                1: {'name': 'ATK flat', 'max_value': 100},
                2: {'name': 'DEF flat', 'max_value': 100},
                3: {'name': 'HP flat', 'max_value': 1500},
                4: {'name': 'SPD', 'max_value': 20}
            }
        },
        2: {
            'name': 'Archetype',
            'types': ['Attack', 'Defense', 'HP', 'Support'],
            'stats': {
                1: {'name': 'ATK%', 'max_value': 10},
                2: {'name': 'DEF%', 'max_value': 10},
                3: {'name': 'HP%', 'max_value': 10},
                4: {'name': 'ACC', 'max_value': 10},
                5: {'name': 'RES', 'max_value': 10}
            }
        }
    }
    
    MONSTER_ATTRIBUTES = {
        1: 'Water',
        2: 'Fire',
        3: 'Wind',
        4: 'Light',
        5: 'Dark'
    }
    
    MONSTER_TYPES = {
        1: 'Attack',
        2: 'Defense',
        3: 'HP',
        4: 'Support'
    }
    
    @classmethod
    def get_monster(cls, unit_id):
        return cls.MONSTERS.get(unit_id, {
            'name': f'Unknown Monster (ID: {unit_id})',
            'element': 'Unknown',
            'type': 'Unknown',
            'stars': 0,
            'family': 'Unknown'
        })
    
    @classmethod
    def get_rune_set(cls, set_id):
        return cls.RUNE_SETS.get(set_id, {
            'name': f'Unknown Set (ID: {set_id})',
            'pieces': 0,
            'effect': 'Unknown effect'
        })
    
    @classmethod
    def get_rune_quality(cls, quality_id):
        return cls.RUNE_QUALITY.get(quality_id, {
            'name': f'Unknown Quality (ID: {quality_id})',
            'color': 'gray'
        })
    
    @classmethod
    def get_rune_stat(cls, stat_id):
        return cls.RUNE_STATS.get(stat_id, {
            'name': f'Unknown Stat (ID: {stat_id})',
            'max_value': 0,
            'grindable': False
        })
    
    @classmethod
    def get_artifact_type(cls, type_id):
        return cls.ARTIFACT_TYPES.get(type_id, {
            'name': f'Unknown Type (ID: {type_id})',
            'elements/types': [],
            'stats': {}
        })
    
    @classmethod
    def get_monster_attribute(cls, attr_id):
        return cls.MONSTER_ATTRIBUTES.get(attr_id, f'Unknown Attribute (ID: {attr_id})')
    
    @classmethod
    def get_monster_type(cls, type_id):
        return cls.MONSTER_TYPES.get(type_id, f'Unknown Type (ID: {type_id})')
    
    @classmethod
    def get_monsters_by_family(cls, family):
        return [mon for mon in cls.MONSTERS.values() if mon['family'] == family]
    
    @classmethod
    def get_monsters_by_element(cls, element):
        return [mon for mon in cls.MONSTERS.values() if mon['element'] == element]
    
    @classmethod
    def get_monsters_by_type(cls, type_):
        return [mon for mon in cls.MONSTERS.values() if mon['type'] == type_]
    
    @classmethod
    def get_monsters_by_stars(cls, stars):
        return [mon for mon in cls.MONSTERS.values() if mon['stars'] == stars]