#The main class, runs the game and takes care of all the housekeeping.

import sys

import Character
import Profession
from professions import Centurion, Carnifex
from items import Longsword, Buckler, HideArmor, ItemLoader
from passive_abilities import IronSkinned, HeroicFortitude, BladeMastery

class Game:
    #takes a list of teams to put into the fight and a map
    def __init__(self, teams, game_map):
        self.teams = teams
        self.events = []
        self.turns = 0
        self.game_map = game_map

    def addEvent(self, event):
        self.events.append(event)
        for team in teams:
            for character in team.characters:
                character.receiveEvent(event)	

class Team:
    #Teams take a list of characters to include
    def __init__(self, characters):
        self.characters = characters    
    
def createSampleTeamOne():
    roster = []
    centurion_character = Character.Character()
    centurion_profession = Centurion.Centurion()
    centurion_profession.apply(centurion_character)
    centurion_character.equipped_shield = Buckler.Buckler()
    centurion_character.equipped_armor = HideArmor.HideArmor()
    iron_skinned = IronSkinned.IronSkinned()
    centurion_character.addPassive(iron_skinned)
    heroic_fortitude = HeroicFortitude.HeroicFortitude()
    centurion_character.addPassive(heroic_fortitude)
    roster.append(centurion_character)
    team = Team(roster)
    return team

def createSampleTeamTwo():
    roster = []
    carnifex_character = Character.Character()
    carnifex_profession = Carnifex.Carnifex()
    carnifex_profession.apply(carnifex_character)
    carnifex_character.equipped_weapon = Longsword.Longsword()
    blade_mastery = BladeMastery.BladeMastery()
    carnifex_character.addPassive(blade_mastery)
    roster.append(carnifex_character)
    team = Team(roster)
    return team

if __name__ == "__main__":
    print "Welcome to Dyne."
    items = ItemLoader.loadItems()
    print items['longsword'].melee_damage_bonus
    teams = [createSampleTeamOne(), createSampleTeamTwo()]
    game = Game(teams, None)
    print "Team 1:"
    for char in game.teams[0].characters:
        print char.profession.name
        char.game = game
    print "Team 2:"
    for char in game.teams[1].characters:
        print char.profession.name
        char.game = game
    centurion = game.teams[0].characters[0]
    carnifex = game.teams[1].characters[0]
    carnifex.basicAttackMelee(centurion)
    
    print centurion.current_hit_points
    
