#!/usr/bin/env python3

"""Who's that Pokemon! """

import os

def pokedex():
    #"define starters"
    starters= [
                {'poke_id': "1",
                 'poke_name': 'Charmander',
                 'poke_type': 'Fire'
                 },


                {'poke_id': "2",
                 'poke_name': 'Squirtle',
                 'poke_type': 'Water'
                 },

    
                {'poke_id': "3",
                 'poke_name': 'Bulbasaur',
                 'poke_type': 'Grass'
                 }
                
              ]
    pick_input = input("Hello Trainer! Choose a type: Fire, Water, or Grass: \n")
    pick_input = pick_input.lower() 


    if pick_input == ("fire"):
            print("\n")
            print(starters[0]["poke_name"])
    elif pick_input == ("water"):
            print(starters[1]["poke_name"])
    elif pick_input == ("grass"):
            print(starters[2]["poke_name"])
    else:
            print ("Sorry, trainer, that is a not a valid starter option for you")




pokedex()
