
import json
import random
from combat import Combat, Pokemon


def display_menu():
    print("13Bienvenue dans le monde des Pokémons ! Que voulez-vous faire ?")
    print("1. Lancer une partie")
    print("2. Ajouter un Pokémon")
    print("3. Accéder à votre Pokédex")
    choice = input("Entrez le numéro de votre choix : ")
    return choice


def load_pokemons():
    with open('pokemon.json') as f:
        data = json.load(f)
    pokemons = []
    for pokemon_data in data:
        pokemon = Pokemon(pokemon_data['name'], pokemon_data['type'], pokemon_data['defense'], pokemon_data['attack'], pokemon_data['hp'])
        pokemons.append(pokemon)
    return pokemons



def add_pokemon():
    name = input("Entrez le nom du Pokémon : ")
    type = input("Entrez le type du Pokémon : ")
    defense = input("Entrez la défense du Pokémon : ")
    attack = input("Entrez la puissance d'attaque du Pokémon : ")
    hp = input("Entrez les points de vie du Pokémon : ")
    pokemon = {"name": name, "type": type,
               "defense": defense, "attack": attack, "hp": hp}
    with open("pokemon.json", "a") as f:
        json.dump(pokemon, f)
        f.write("\n")
    print("Le Pokémon a été ajouté avec succès !")


def display_pokedex(pokemons):
    for pokemon in pokemons:
        print(
            f"Nom : {pokemon['name']}, Type : {pokemon['type']}, Défense : {pokemon['defense']}, Attaque : {pokemon['attack']}, Points de vie : {pokemon['hp']}")


def choose_pokemon():
    pokemons = load_pokemons()
    print("Choisissez votre Pokémon :")
    for index, pokemon in enumerate(pokemons):
        print(f"{index + 1}. {pokemon['name']} ({pokemon['type']})")
    choice = int(input("Entrez le numéro de votre choix : "))
    return pokemons[choice - 1]


def choose_opponent():
    pokemons = load_pokemons()
    return random.choice(pokemons)


def main():
    while True:
        choice = display_menu()
        if choice == "1":
            player_pokemon = choose_pokemon()
            opponent_pokemon = choose_opponent()
            combat = Combat(player_pokemon, opponent_pokemon)
            combat.start_combat()
        elif choice == "2":
            add_pokemon()
        elif choice == "3":
            pokemons = load_pokemons()
            display_pokedex(pokemons)
        else:
            print("Choix invalide !")


if __name__ == "__main__":
    main()
