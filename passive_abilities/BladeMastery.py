class BladeMastery:
    def __init__(self):
        self.name = "Blade Mastery"
        self.type = "conditional_stat_bonus"
        self.melee_damage_bonus = 1

    def checkCondition(self, character):
        if character.equipped_weapon is not None:
            if character.equipped_weapon.item_subtype is "blade":
                return True
        return False
