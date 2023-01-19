#! /usr/bin/env python3

"""This file is used to outline the layout and track the inventory of the user inputs during their journey in the deepspace rpg.
If the user obtains an item or does a necessary tasks, the value of the key will change to 1. If the value of an item is 1, it will be added
to the users inventory, otherwise, if the value is 1, and that value is necessary to access a separate section, the access will be granted."""


#the back of the ship contains 3 rooms
back_of_ship = {
    "cryo_chamber": {
        "table": 0,   #on the table is a hint to the combination of the keypad / numlock
        "suit": 0,    #the suit is necessary to leave the room
        "keypad": 0   #the combination to the keypad is found on a note on the table
        },

    "docking_bay": {  #the docking bay is directly across from the cryo chamber - "go forward"
        "pressure_pad": 0,  #to access the pressurization padlock, you must have the oxygen suit (EMU)
        "door": 0            #door to the docking bay is locked - MISSION SPECIALIST door: 1 = unlocked
        },

    "engine_room": { #the engine room is to the RIGHT when stepping out of cryo, and LEFT when stepping out of docking bay
        "key": 0,    #door to engine room is locked - FLIGHT ENGINEER
        "wires": 0   #wire combination can be guessed, with incorrect guessing resulting in death. Combination is found in flight engineer notes
        }
    }



mid_ship_one = {
    "miss_spec": {   #mission specialist room found on RIGHT when entering primary cooridor of ship
        "door": 0,   #door locked unless role = miss_spec
        "key": 0,    #key in miss_spec room unlocks docking bay
        "emu_suit": 0,  #emu suit needed to go to pressure_pad
        "journal": 0    #journal under pillow - ACHIEVEMENT
        },

    "flight_eng": {  #flight engineer room found on LEFT when entering primary cooridor of ship
        "door": 0,   #door is locked without key or if the user is assigned flight_eng role
        "safe": 0,   #safe combination is found in notes. Safe is at the bottom of bookshelf
        "notes": 0   #notes are 3 pages, also includes WIRES combination for engine_room
        }
    }


mid_ship_two = {
    "pilot": {
        "door": 0,  #door is locked unless user has pilot role
        "vent": 0,  #vent can be climbed into to access pilots room if they don't have role
        "key": 0,   #key unlocks flight deck
        "notes": 0, #notes for navigation system on flight deck
        "journal": 0 #journal in desk drawer - ACHIEVEMENT
        },

    "sci_officer": {
        "door": 0,  #door locked unless user has sci_officer key LAB or user has role
        "safe": 0,  #safe combination found in notes
        "notes": 0  #notes have oxygen stabilization commands for LAB
        }
    }


mid_ship_three = {
    "commanders_room": {},

    "lab": {
        "sci_office_key": 0, #sci_officer key for sci_officer room
        "doc_notes": 0,      #doc_notes detail mission goals
        "oxy_suit": 0,       #oxy_suit to enter flight deck
        "journal": 0,         #journal behind samples ACHIEVEMENT
        "upload": 0           #upload / save ?
        }
    }


flight_deck = {
        "nav_portal" : {
            "nav_commands": 0 #nav commands found in pilots room

            }
        }

