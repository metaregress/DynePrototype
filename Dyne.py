#The main class, runs the game and takes care of all the housekeeping. I'm probably going to keep all the classes here until it gets too hairy, then break them out as needs be

import sys

class Game:
    #only takes a list of teams to put into the fight
    def __init__(self, teams):
        self.teams = teams
        self.events = []
        self.turns = 0	

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
        #split into nerfs/buffs? :\
        self.status_effects = []
        self.speed = 0
        self.hit_points = 0
        self.base_damage = 1
        self.init_tokens = 1

    def move(self, destination):
        #check 
        pass

    #takes another Character as a target
    def basicAttack(self, target):
        pass

def createSampleTeam():
    pass

if __name__ == "__main__":
    print "Welcome to Dyne."
