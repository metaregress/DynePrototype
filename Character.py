import Dyne
import DamageDealtEvent

class Character:
    #I'm gonna start em naked
    #down the line I'd like to be able to use JSON here to give fast stats
    #not sure what to do about classes; just compose it? or what?
    def __init__(self):
        #make some of these CONST?
        self.active_ability_cap = 4
        self.passive_ability_cap = 3
        self.gold = 10
        self.action_points = 5
        self.active_abilities = {}
        self.passive_abilities = {}
        self.inventory = {}
        self.equipped_weapon = None
        self.equipped_armor = None
        self.equipped_shield = None
        #split into nerfs/buffs? :\
        self.status_effects = {}
        self.movement = 0
        self.current_hit_points = 0
        self.max_hit_points = 0
        self.base_melee_damage = 1
        self.base_ranged_damage = 1
        self.initiative_tokens = 1
        self.position_x = 0
        self.position_y = 0
        self.profession = None
        self.profession_ability = None
        self.armor = 0
        self.protection = 0
        self.game = None
        #move these into profession...?
        self.resource = 0
        self.resource_name = ""

    def receiveEvent(self, event):
        if self.profession_ability:
            self.profession_ability(self, event)    
    
    def addPassive(self, passive_ability):
        if len(self.passive_abilities) >= 3:
            print "too many passives"
        else:
            self.passive_abilities[passive_ability.name] = passive_ability
            if passive_ability.type == "consumable_stat_bonus":
                passive_ability.apply(self)

    def move(self, destination):
        #check distance to make sure it's within range
        pass
    
    def getTotalMeleeDamage(self):
        total_damage =  self.base_melee_damage + self.profession.melee_damage_bonus
        if self.equipped_weapon is not None:
            total_damage += self.equipped_weapon.melee_damage_bonus
        if self.passive_abilities is not {}:
            for passive_name in self.passive_abilities:
                passive = self.passive_abilities[passive_name]
                if passive.type is "stat_bonus":
                    if hasattr(passive, "melee_damage_bonus"):
                        total_damage += passive.melee_damage_bonus
                elif passive.type is "conditional_stat_bonus":
                    if hasattr(passive, "melee_damage_bonus"):
                        if passive.checkCondition(self):
                            total_damage += passive.melee_damage_bonus
                        
        return total_damage

    def getTotalRangedDamage(self):
        total_damage = self.base_ranged_damage + self.profession.ranged_damage_bonus
        if self.equipped_weapon is not None:
            total_damage += self.equipped_weapon.ranged_damage_bonus
        return total_damage
    
    def getTotalArmor(self):
        total_armor = self.armor
        if self.equipped_armor is not None:
            total_armor += self.equipped_armor.armor_bonus
        if self.equipped_shield is not None:
            total_armor += self.equipped_shield.armor_bonus
        if self.passive_abilities is not {}:
            for passive_name in self.passive_abilities:
                passive = self.passive_abilities[passive_name]
                if passive.type is "stat_bonus":
                    if hasattr(passive, "armor_bonus"):
                        total_armor += passive.armor_bonus
        return total_armor

    #takes another Character as a target
    def basicAttackMelee(self, target):
        damage_dealt = self.getTotalMeleeDamage() - target.getTotalArmor()
        target.current_hit_points -= damage_dealt
        self.game.addEvent(DamageDealtEvent.DamageDealtEvent(self, target, damage_dealt, "melee"))

    def basicAttackRanged(self, target):
        damage_dealt = self.getTotalRangedDamage() - target.getTotalArmor()
        target.current_hit_points -= damage_dealt
        self.game.addEvent(DamageDealtEvent.DamageDealtEvent(self, target, damage_dealt, "ranged"))
