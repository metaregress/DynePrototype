import Profession
import DamageDealtEvent 

def centurionAbility(self, event):
    if type(event) is DamageDealtEvent:
        if event.recipient is self:
            print "I'm hit!"

#I know doing this makes me a  dummy. gotta go fast
def Centurion():
    centurion_ability = centurionAbility
    centurion_dict = {'profession_ability': centurion_ability, 'basic_attack_melee_delta': 0, 'basic_attack_ranged_delta': 0, 'movement_delta': 4, 'hit_points': 45, 'initiative_token_delta': 1, 'name': 'Centurion'}
    centurion_profession = Profession.Profession(centurion_dict)
    return centurion_profession
