# unit.py

class Unit:
    def __init__(self, unit_id, wizard_id, island_id, pos_x, pos_y, building_id, unit_master_id, unit_level, 
                 class_type, con, atk, def_, spd, resist, accuracy, critical_rate, critical_damage, 
                 experience, exp_gained, exp_gain_rate, skills, runes, artifacts, costume_master_id, trans_items, 
                 attribute, create_time, source, homunculus, homunculus_name, unit_index, awakening_info):
        self.unit_id = unit_id
        self.wizard_id = wizard_id
        self.island_id = island_id
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.building_id = building_id
        self.unit_master_id = unit_master_id
        self.unit_level = unit_level
        self.class_type = class_type
        self.con = con
        self.atk = atk
        self.def_ = def_
        self.spd = spd
        self.resist = resist
        self.accuracy = accuracy
        self.critical_rate = critical_rate
        self.critical_damage = critical_damage
        self.experience = experience
        self.exp_gained = exp_gained
        self.exp_gain_rate = exp_gain_rate
        self.skills = skills
        self.runes = runes
        self.artifacts = artifacts
        self.costume_master_id = costume_master_id
        self.trans_items = trans_items
        self.attribute = attribute
        self.create_time = create_time
        self.source = source
        self.homunculus = homunculus
        self.homunculus_name = homunculus_name
        self.unit_index = unit_index
        self.awakening_info = awakening_info

    @classmethod
    def from_json(cls, json_data):
        return cls(
            unit_id=json_data["unit_id"],
            wizard_id=json_data["wizard_id"],
            island_id=json_data["island_id"],
            pos_x=json_data["pos_x"],
            pos_y=json_data["pos_y"],
            building_id=json_data["building_id"],
            unit_master_id=json_data["unit_master_id"],
            unit_level=json_data["unit_level"],
            class_type=json_data["class"],
            con=json_data["con"],
            atk=json_data["atk"],
            def_=json_data["def"],  # "def" est un mot réservé, donc on utilise "def_" comme nom de variable
            spd=json_data["spd"],
            resist=json_data["resist"],
            accuracy=json_data["accuracy"],
            critical_rate=json_data["critical_rate"],
            critical_damage=json_data["critical_damage"],
            experience=json_data["experience"],
            exp_gained=json_data["exp_gained"],
            exp_gain_rate=json_data["exp_gain_rate"],
            skills=json_data["skills"],
            runes=json_data["runes"],
            artifacts=json_data["artifacts"],
            costume_master_id=json_data["costume_master_id"],
            trans_items=json_data["trans_items"],
            attribute=json_data["attribute"],
            create_time=json_data["create_time"],
            source=json_data["source"],
            homunculus=json_data["homunculus"],
            homunculus_name=json_data["homunculus_name"],
            unit_index=json_data["unit_index"],
            awakening_info=json_data["awakening_info"]
        )
