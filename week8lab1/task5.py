import random
from abc import ABC, abstractmethod
import math

class GeneralClass(ABC):
    character_tuple = ('Knight', 'Mage', 'Super Mage')
    move_list = ['regular_attack']

    def __init__(self):
        self.name = None
        self.health = None
        self.power = None
        self.move_list = GeneralClass.move_list.copy()
        self.death_cry = None

    def get_hit(self, damage):
        self.health = max(self.health - damage, 0)
        if self.health == 0:
            print(f"{self.name} says: {self.death_cry}")

    @abstractmethod
    def hit(self, move):
        pass

class KnightClass(GeneralClass):
    def __init__(self):
        super().__init__()
        self.name = "Knight"
        self.health = 13
        self.power = 4
        self.move_list = ['regular_attack', 'spear_attack']
        self.death_cry = 'Arrrrgh!'

    def hit(self, move):
        if move == 'regular_attack':
            return math.ceil(self.power * 1.0)
        elif move == 'spear_attack':
            return math.ceil(self.power * 1.7)

class MageClass(GeneralClass):
    def __init__(self):
        super().__init__()
        self.name = "Mage"
        self.health = 22
        self.power = 3
        self.move_list = ['regular_attack', 'spell_attack']
        self.death_cry = 'Noooo!'

    def hit(self, move):
        if move == 'regular_attack':
            return math.ceil(self.power * 1.0)
        elif move == 'spell_attack':
            return math.ceil(self.power * 1.8)

class SuperMageClass(MageClass):
    def __init__(self):
        super().__init__()
        self.name = "Super Mage"
        self.health = 24
        self.power = 4
        self.move_list = ['regular_attack', 'spell_attack', 'super_spell_attack']
        self.death_cry = '-.-'

    def hit(self, move):
        if move == 'regular_attack':
            return math.ceil(self.power * 1.0)
        elif move == 'spell_attack':
            return math.ceil(self.power * 1.8)
        elif move == 'super_spell_attack':
            return math.ceil(self.power * 2.2)

def instantiate_character(character_name):
    if character_name == 'Knight':
        return KnightClass()
    elif character_name == 'Mage':
        return MageClass()
    elif character_name == 'Super Mage':
        return SuperMageClass()

def rand_move(player):
    move = random.choice(player.move_list)
    print(f"{player.name} uses {move}")
    return move

def battle(player1, player2):
    turn = 0
    while player1.health > 0 and player2.health > 0:
        if turn % 2 == 0:
            print(f"\nPlayer 1 ({player1.name}) - Health: {player1.health}")
            move1 = rand_move(player1)
            damage1 = player1.hit(move1)
            print(f"{player1.name} dealt {damage1} damage to {player2.name}.")
            player2.get_hit(damage1)
        else:
            print(f"\nPlayer 2 ({player2.name}) - Health: {player2.health}")
            move2 = rand_move(player2)
            damage2 = player2.hit(move2)
            print(f"{player2.name} dealt {damage2} damage to {player1.name}.")
            player1.get_hit(damage2)

        print(f"Player 1 Health: {player1.health}, Player 2 Health: {player2.health}")
        turn += 1

    if player1.health == 0:
        print(f"\n{player1.name} has been defeated. {player2.name} wins!")
    else:
        print(f"\n{player2.name} has been defeated. {player1.name} wins!")

player1 = instantiate_character('Knight')
player2 = instantiate_character('Mage')

print(f"Player 1: {player1.name}, Health: {player1.health}")
print(f"Player 2: {player2.name}, Health: {player2.health}")

battle(player1, player2)
