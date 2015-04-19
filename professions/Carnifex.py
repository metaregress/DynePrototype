import Profession

def Carnifex():
    carnifex_ability = None
    carnifex_dict = {'profession_ability': carnifex_ability, 'basic_attack_melee_delta': 2, 'basic_attack_ranged_delta': 0, 'movement_delta': 5, 'hit_points': 35, 'initiative_token_delta': 2, 'name': 'Carnifex'}
    carnifex_profession = Profession.Profession(carnifex_dict)
    return carnifex_profession
