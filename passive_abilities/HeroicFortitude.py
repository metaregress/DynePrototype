class HeroicFortitude():
    def __init__(self):
        self.name = "Heroic Fortitude"
        self.type = "consumable_stat_bonus"

    def apply(self, character):
        character.max_hit_points += 10
        character.current_hit_points += 10
