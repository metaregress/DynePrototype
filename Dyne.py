#The main class, runs the game and takes care of all the housekeeping. I'm probably going to keep all the classes here until it gets too hairy, then break them out as needs be

import sys

class Game:
    #takes a list of teams to put into the fight and a map
    def __init__(self, teams, game_map):
        self.teams = teams
        self.events = []
        self.turns = 0
        self.game_map = game_map	

class Team:
    #Teams take a list of characters to include
    def __init__(self, characters):
        self.characters = characters    

class Character:
    #I'm gonna start em naked
    #down the line I'd like to be able to use JSON here to give fast stats
    #not sure what to do about classes; just compose it? or what?
    def __init__(self):
        #make some of these CONST?
        self.active_cap = 4
        self.passive_count = 3
        self.gold = 10
        self.action_points = 5
        self.actives = []
        self.passives = []
        self.equipment = []
        #split into nerfs/buffs? :\
        self.status_effects = []
        self.movement = 0
        self.hit_points = 0
        self.base_damage_melee = 1
        self.base_damage_ranged = 1
        self.initiative_tokens = 1
        self.position_x = 0
        self.position_y = 0
        self.profession = None
        self.profession_ability = None
        self.armor = 0
        self.protection = 0

    def move(self, destination):
        #check distance to make sure it's within range
        pass

    #takes another Character as a target
    def basicAttackMelee(self, target):
        target.hit_points -= self.base_damage_melee - target.armor

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

def createSampleTeamOne():
    roster = []
    centurion_character = Character()
    centurion_profession = Centurion()
    centurion_profession.apply(centurion_character)
    roster.append(centurion_character)
    team = Team(roster)
    return team

def createSampleTeamTwo():
    roster = []
    carnifex_character = Character()
    carnifex_profession = Carnifex()
    carnifex_profession.apply(carnifex_character)
    roster.append(carnifex_character)
    team = Team(roster)
    return team

#I know doing this makes me a  dummy. gotta go fast
def Centurion():
    centurion_ability = None
    centurion_dict = {'profession_ability': centurion_ability, 'basic_attack_melee_delta': 0, 'basic_attack_ranged_delta': 0, 'movement_delta': 4, 'hit_points': 45, 'initiative_token_delta': 1, 'name': 'Centurion'}
    centurion_profession = Profession(centurion_dict)
    return centurion_profession

def Carnifex():
    carnifex_ability = None
    carnifex_dict = {'profession_ability': carnifex_ability, 'basic_attack_melee_delta': 2, 'basic_attack_ranged_delta': 0, 'movement_delta': 5, 'hit_points': 35, 'initiative_token_delta': 2, 'name': 'Carnifex'}
    carnifex_profession = Profession(carnifex_dict)
    return carnifex_profession

if __name__ == "__main__":
    print "Welcome to Dyne."
    teams = [createSampleTeamOne(), createSampleTeamTwo()]
    game = Game(teams, None)
    print "Team 1:"
    for char in game.teams[0].characters:
        print char.profession
    print "Team 2:"
    for char in game.teams[1].characters:
        print char.profession

    centurion = game.teams[0].characters[0]
    carnifex = game.teams[1].characters[0]
    centurion.basicAttackMelee(carnifex)
    print carnifex.hit_points

