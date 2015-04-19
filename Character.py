import Dyne
import DamageDealtEvent

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
        self.game = None
        self.resource = 0
        self.resource_name = ""

    def receiveEvent(self, event):
        if self.profession_ability:
            self.profession_ability(self, event)    
    def move(self, destination):
        #check distance to make sure it's within range
        pass

    #takes another Character as a target
    def basicAttackMelee(self, target):
        damage_dealt = self.base_damage_melee - target.armor
        target.hit_points -= damage_dealt
        self.game.addEvent(DamageDealtEvent.DamageDealtEvent(self, target, damage_dealt))
