import Profession
import DamageDealtEvent 
import json

def centurionAbility(self, event):
    if type(event) is DamageDealtEvent:
        if event.recipient is self:
            print "I'm hit!"

#I know doing this makes me a  dummy. gotta go fast
def Centurion():
   # centurion_dict = {'profession_ability': centurion_ability, 'basic_attack_melee_delta': 0, 'basic_attack_ranged_delta': 0, 'movement_delta': 4, 'hit_points': 45, 'initiative_token_delta': 1, 'name': 'Centurion'}
    centurion_profession = None
    with open('professions/centurion.json', 'r') as data_file:    
        centurion_dict = json.load(data_file)
        centurion_ability = centurion_dict['profession_ability'] = centurionAbility
        centurion_profession = Profession.Profession(centurion_dict)
    return centurion_profession
