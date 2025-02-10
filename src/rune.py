# rune.py
class Rune:
    def __init__(self, rune_id, wizard_id, occupied_type, occupied_id, slot_no, rank, 
                 class_type, set_id, upgrade_limit, upgrade_curr, base_value, sell_value, 
                 pri_eff, prefix_eff, sec_eff, extra):
        self.rune_id = rune_id
        self.wizard_id = wizard_id
        self.occupied_type = occupied_type
        self.occupied_id = occupied_id
        self.slot_no = slot_no
        self.rank = rank
        self.class_type = class_type
        self.set_id = set_id
        self.upgrade_limit = upgrade_limit
        self.upgrade_curr = upgrade_curr
        self.base_value = base_value
        self.sell_value = sell_value
        self.pri_eff = pri_eff
        self.prefix_eff = prefix_eff
        self.sec_eff = sec_eff
        self.extra = extra

    @classmethod
    def from_json(cls, json_data):
        return cls(
            rune_id=json_data["rune_id"],
            wizard_id=json_data["wizard_id"],
            occupied_type=json_data["occupied_type"],
            occupied_id=json_data["occupied_id"],
            slot_no=json_data["slot_no"],
            rank=json_data["rank"],
            class_type=json_data["class"],
            set_id=json_data["set_id"],
            upgrade_limit=json_data["upgrade_limit"],
            upgrade_curr=json_data["upgrade_curr"],
            base_value=json_data["base_value"],
            sell_value=json_data["sell_value"],
            pri_eff=json_data["pri_eff"],
            prefix_eff=json_data["prefix_eff"],
            sec_eff=json_data["sec_eff"],
            extra=json_data["extra"]
        )