class Profession:
    #so for now I'm going with the idea that professions are added onto a Character; we'll see how this plays out 
    #constructor takes a dict of parameters, see the code to see names expected
    def __init__(self, details):
        self.profession_ability = details['profession_ability']
        self.melee_damage_bonus = details['melee_damage_bonus']
        self.ranged_damage_bonus = details['ranged_damage_bonus']
        self.movement_bonus = details['movement_bonus']
        self.hit_points = details['hit_points']
        self.name = details['name']
        self.initiative_token_bonus = details['initiative_token_bonus']

    #rather than assigning everything here to modify the base values, I'm going to simply reference them from within Character.
    def apply(self, character):
        character.profession = self
        character.hit_points = self.hit_points
        character.profession_ability = self.profession_ability
        #character.profession = self.name
        #character.profession_basic_damage_melee += self.basic_attack_melee_delta
        #character.profession_basic_damage_ranged += self.basic_attack_ranged_delta
        #character.hit_points = self.hit_points
        #character.movement += self.movement_delta
        #character.profession_ability = self.profession_ability
        #character.initiative_tokens += self.initiative_token_delta
