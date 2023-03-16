import random
import json

class Combat:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.current_pokemon = None
        self.opponent_pokemon = None
        self.winner = None

    def start_combat(self):
        print(f"Un combat debute entre {self.pokemon1} et {self.pokemon2} !")
        self.current_pokemon = self.pokemon1
        self.opponent_pokemon = self.pokemon2

        while self.winner is None:

            self.current_pokemon.get_attack_damage(self.opponent_pokemon, attack)

            if self.opponent_pokemon.hp == 0:
                self.winner = self.current_pokemon
                break

            
            self.current_pokemon, self.opponent_pokemon = self.opponent_pokemon, self.current_pokemon

        print(f"{self.winner} remporte le combat !")


class Pokemon:
    def __init__(self, name, hp=100, level=1, attack=0, defense=0):
        self.name = name
        self.hp = hp
        self.level = level
        self.attack = attack
        self.defense = defense

    def __str__(self):
        return f"{self.name} (niveau {self.level})"

    def get_attack_damage(self, opponent):
        attack_modifier = self.get_attack_modifier(opponent.type)
        damage = self.attack * attack_modifier
        opponent.hp -= damage
        if opponent.hp < 0:
            opponent.hp = 0
        print(f"{self.name} attaque {opponent.name} et lui inflige {damage} degats")
        if opponent.hp == 0:
            print(f"{opponent.name} est K.O. {self.name} remporte le combat !")

    def get_attack_modifier(self, opponent_type):
        return 1.0  


class NormalPokemon(Pokemon):
    def __init__(self, name, hp=100, level=1, attack=0, defense=0):
        super().__init__(name, hp, level, attack, defense)
        self.type = "normal"
        self.hp = hp
        self.attack = 15
        self.defense = 15

    def get_attack_modifier(self, opponent_type):
        if opponent_type == "normal":
            return 1
        else:
            return 0.75


class FirePokemon(Pokemon):
    def __init__(self, name, hp=100, level=1, attack=0, defense=0):
        super().__init__(name, hp, level, attack, defense)
        self.type = "fire"
        self.attack = 20
        self.defense = 10

    def get_attack_modifier(self, opponent_type):
        if opponent_type == "water":
            return 0.5
        elif opponent_type == "ground":
            return 2.0
        else:
            return 1.0


class WaterPokemon(Pokemon):
    def __init__(self, name, hp=100, level=1, attack=0, defense=0):
        super().__init__(name, hp, level, attack, defense)
        self.type = "water"
        self.hp = hp
        self.defense = 20
        self.attack = 10

    def get_attack_modifier(self, opponent_type):
        if opponent_type == "fire":
            return 2.0
        elif opponent_type == "ground":
            return 0.5
        else:
            return 1.0



class GroundPokemon(Pokemon):
    def __init__(self, name, hp=100, level=1, attack=0, defense=0):
        super().__init__(name, hp, level, attack, defense)
        self.type = "ground"
        self.hp = hp
        self.defense = 23
        self.attack = 7

    def get_attack_modifier(self, opponent_type):
        if opponent_type == "water":
            return 2.0
        elif opponent_type == "fire":
            return 0.5
        else:
            return 1.0
