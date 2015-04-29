class Item:
    def __init__(self, details):
        self.price = details['price']
        self.item_type = details['item_type']
        self.equippable = details['equippable']
        self.armor_bonus = details['armor_bonus']
        self.protection_bonus = details['protection_bonus']
        self.melee_damage_bonus = details['melee_damage_bonus']
        self.ranged_damage_bonus = details['ranged_damage_bonus']
        self.ability = None
