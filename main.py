from pokemon import Pokemon
from moves import Moves
import json
import random

list_j1 = []
list_j2 = []
moves_list = []

with open("pokemon.json", "r", encoding='utf-8') as f:
    pokemon_list = json.load(f)

def get_three_random_pokemon():
    choice_list = {}
    for i in range(3):
        rand = random.randint(1, len(pokemon_list) - 1)
        choice_list[i] = pokemon_list[rand]['name']['french']
    
    return choice_list

def main():
    
    print("-" * 60 + "\n" + " " * 23 + "POKEMON BATTLE" + "\n" + "-" * 60 + "\n")
    
    for i in range (0, 3):
        print("J1 : Choisissez un de ces trois Pokemon à ajouter à votre équipe")
        result = get_three_random_pokemon()
        for i in result:
            print(f"{i + 1}: {result.get(i)}")
        choix = input("Votre choix : ")
        list_j1.append(result.get(int(choix) - 1))
    
    print(list_j1)
    
main()