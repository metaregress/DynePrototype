class Profession:
    #so for now I'm going with the idea that professions are added onto a Character; we'll see how this plays out 
    #constructor takes a dict of parameters, see the code to see names expected
    def __init__(self, details):
        self.profession_ability = details['profession_ability']
        self.basic_attack_melee_delta = details['basic_attack_melee_delta']
        self.basic_attack_ranged_delta = details['basic_attack_ranged_delta']
        self.movement_delta = details['movement_delta']
        self.hit_points = details['hit_points']
        self.name = details['name']
        self.initiative_token_delta = details['initiative_token_delta']

    def apply(self, character):
        character.profession = self.name
        character.base_damage_melee += self.basic_attack_melee_delta
        character.base_damage_ranged += self.basic_attack_ranged_delta
        character.hit_points = self.hit_points
        character.movement += self.movement_delta
        character.profession_ability = self.profession_ability
        character.initiative_tokens += self.initiative_token_delta
