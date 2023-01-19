#! /usr/bin/env python3

import random
import os
import time
import sys
sys.path.append('/mycode/deepspacerpg')
import ship_layout
from termcolor import cprint

pause = 0.058

#B.E.N. typing effect
def ben(word: str):
    for i in word:
        time.sleep(pause)
        print(i, end="", flush = True)


#crew variables for assignment
crew = {'Science Officer': "Carson Beckett",
        'Pilot': "Jane Smith",
        'Mission Specialist': "Bob Johnson",
        'Flight Engineer': "Emily Davis"}
name = ''

def start():

    global name

    os.system('clear') #clear screen
    ben("Hello, Cosmonaut. My systems have malfunctioned and I am unable to access your biometric data. Please remind me who you are? ") #take username CHANGE?*
    name = input("> ")
    os.system('clear') #clear screen
    ben("""
        ...inputting
        ...
        ...uploading
        ...scanning biometric archives
        ...crewmate found""")
    ben(f"\nName: {name}. Role {role}\n")
    time.sleep(2)
    os.system('clear') #clear screen
    time.sleep(1.5)

    from ds_title import title
    title()
    time.sleep(1)
    input("Press any key to begin")


# Clear the screen after getting user input
os.system('clear')

# Assign user name to a random crewmember
role = random.choice(list(crew.keys()))
crew[role] = name #role variable will match randomly generated choice

inventory = [] #list to track inventory

#inventory tracking function - allows user to print their inventory at any time
def show_inventory():
    if not inventory:
        ben("There are currently no items in your inventory")
    else:
        print("You currently carry: ")
        for item in inventory:
            print('*', item)


#called from the while loop - prints user role
def check_role():

    global role

    ben(f"You are the {role} aboard this craft.\n")
    return

#randomly generated code specifically for cryo_chamber_keypad
cryo_chamber_keypad = "".join(str(random.randint(0,9)) for _ in range(5))

#works in conjuction with cryo_pod() after user unlocks the pod. This still occurs prior to countdown timer
def cryo_chamber():
    
    global cryo_chamber_keypad
    global inventory

    has_code = False
    has_suit = False

    os.system('clear')

    ben(f"Great job {name}. Now let's see if we can find a way out of the cryo_chamber and into the ship. It seems that the engine's have failed. The navigations systems appear to be offline, and the autopilot cannot reroute us. We must find the problem with the engines and reset the navigation portal.\n")

    print(f"\n\033[3m You step out of the pod into a small room. To the left and right of the pod are those of your crewmmates, life-system monitors blinking red. In front of you is a table. On the other side of the table is a row of hanging suits. To your left is a door, with a digital numlock keypad next to it. \033[23m")

    while True:

        u_choice = input("\nWhat would you like to do? \n\n>")

        if "look" in u_choice.lower() or "cryo" in u_choice.lower():
            ben("We don't have time")

        elif "walk" in u_choice.lower() and "table" in u_choice.lower(): #walk to table to pick up not
            print(f"\n\033[3mYou walk to the table and examine the notes. One stands out with a series of numbers on it\033[23m \n")
            note_take = (input("What would you like to do? > ")) #user input to add note to inventory
            if note_take.lower() == "take note" or note_take.lower() == "read note":
                has_code = True
                ship_layout.back_of_ship["cryo_chamber"]["table"] = 1
                inventory.append(f"keycode {cryo_chamber_keypad}")
                print(f"\nThe note contains the following combination: {cryo_chamber_keypad}\n")

        elif "suits" in u_choice.lower():
            print(f"\n\033[3mYou walk over to the suits. One of the suits has your name on it: {name} \nWould you like to put on the suit?\033[23m \n")
            suit_on = input("yes / no:: > ")
            if suit_on.lower() == 'yes' or suit_on.lower() == 'y':
                has_suit = True
                inventory.append("suit")
                print("\n\033[3mYou put on the suit\033[23m\n")
            else:
                print("\n\033]3mYou need clothing!\033[23m\n")

        elif "door" in u_choice.lower():
            if "suit" in inventory and f"keycode {cryo_chamber_keypad}" in inventory:
                print("\n\033[3mYou walk to the door and stand in front of the dimly lit digital keypad lock\033[23m\n")
                keypad_choice = input("Enter Combination::")
                count = 3
                if keypad_choice == cryo_chamber_keypad:
                    break
                    return
                else:
                    count -= 1
                    print(f"\nIncorrect code. Remaining number of attempts: {count}")
            else:
                print("\n\033[3mYou are missing an item before you can leave the cryo-chamber\033[23m\n")
        else:
            print("\nInvalid choice, please try again.")




#called after start, this function will act as the 'tutorial phase' for the user. After this function ends, the countdown begins
def cryo_pod():
    
    os.system('clear')

    ben(f"{name}........wake up {name}... ...")
    ben("\nOh good...you're awake")

    time.sleep(1)
    print('-')
    print(f"\n\033[3m You awaken inside a pod-like chamber, lights are flashing and the feint sound of an alarm is going off in the distance\033[23m")
    print('-')
    print(input("Press any key to continue"))
    os.system('clear')

    ben(f"{name}, I am B.E.N., the Bio-Enhanced Navigator. You and your other crew mates were in Cryo sleep during our interstellar journey to Andromeda. Unfortunately, my scans indicate you are the only current survivor of the ship.\nScans show severe system damage and imminent failure if not repaired. You must repair the ship and rechart our course before complete system failure, please remove yourself from the cryopod quickly as we don't have much time.\n")

    print(f"\n\033[3m As your eyes adjust, you realize you are in a cryo-sleep pod. Above you is a monitor with two digitally blinking eyes, it's B.E.N. In front of you is a foggy glass window. You look down and see a latch. \033[23m")
    
    #loop will introduce user to commands, hints will be introduced after
    while True:
        u_choice = input("\n\nWhat would you like to do?\n\n>")
        if "talk" in u_choice.lower() or "ben" in u_choice.lower():
            ben("You must break out of the Cryo-Pod")
        elif "wipe" in u_choice.lower() or "window" in u_choice.lower():
            print(f"\n\033[3m You wipe the glass in front of you, beyond it is what appears to be a room. A table sits at the center of the room, scattered with what appears to be notes and charts. A row of suits hang on a rack beyond the table. To the right is a door with a flashing red light above it. \033[23m \n")
        elif "turn" in u_choice.lower() or "latch" in u_choice.lower():
            print(f"\n\033The cryo-pod hisses as the door swings open \033[23m \n")
            cryo_chamber()
            return
        else:
            print("\nInvalid choice, please try again.")


#assign initial keys from ship_layout file
if role == "Mission Specialist":
    ship_layout.mid_ship_one["miss_spec"]["key"] = 1
    inventory.append("Mission Specialist Key")
elif role == "Flight Engineer":
    ship_layout.mid_ship_one["flight_eng"]["door"] = 1
    inventory.append("Flight Engineer Key")
elif role == "Pilot":
    ship_layout.mid_ship_two["pilot"]["door"] = 1
    inventory.append("Pilot Key")
elif role == "Science Officer":
    ship_layout.mid_ship_two["sci_officer"]["door"] = 1
    inventory.append("Science Officer Key")


def room():

    global inventory



    print(f"\n\033[3m You enter your room. An end table sits next to a seemingly unused bed. On the table is something shiny. \033[23m\n")

    walked_to_table = False
    while True:
        u_input = input("> ")
        if u_input.lower() == "walk" or u_input.lower() == "table":
            print("You walk over to the table. On it is a key")
            walked_to_table = True
        elif walked_to_table and u_input.lower() == "take key":
            inventory.append("flight deck key")
            print("You take the key and leave the room.")
            return
        elif not walked_to_table and u_input.lower() == "take key":
            print("You need to walk over to the table first.")
        else:
            print("Invalid input.")
    
    return


def flight_deck():

    os.system('clear')

    print("You have made it to the flight deck. Would you like to restart all systems and correct navigation?")

    choice = input("Yes? > ")

    if choice.lower() == 'y' or choice.lower() == 'yes':
        os.system('clear')
        print("YOU WIN")
        sys.exit()



#map is called from within countdown timer function as is passed an argument of 'map' or 'move'
def map(action):

    global role

    rooms = {
        1: "Flight Deck",
        2: "Lab",
        3: "Mission Specialist's Room",
        4: "Science Officer's Room",
        5: "Pilot's Room",
        6: "Flight Engineer Room",
        7: "Engine Room",
        8: "Cryo Chamber"
    }

    if action.lower() == "map":
        for key in rooms:
            print(f"{key}. {rooms[key]}")
        return
    elif action.lower() == "move":
        for key in rooms:
            print(f"{key}. {rooms[key]}")
        choice = input("\nWhere would you like to go? Select a room number: >")
        if role == "Science Officer" and choice == "4":
            room()
            return
        elif role == "Pilot" and choice == "5":
            room()
            return
        elif role == "Mission Specialist" and choice == "3":
            room()
            return
        elif role == "Flight Engineer" and choice == "6":
            room()
            return
        elif "flight deck key" in inventory and choice == "1":
            flight_deck()
        else:
            print("You don't have the necessary items to access this room")
            return



def ben_final():

    os.system('clear')

    ben(f"{name}, scans indicate imminent power failure in approximately 5 minutes. The ship's systems will automatically divert all power to necessary resources. I am going offline. With your suit, you have access to the ships primary Map log. Use it to navigate to the appropriate part of the ship and restore systems. Best of luck, cosmonaut.\n")

    time.sleep(1.5)

    return

#countdown timer begins at the beginning of the game, counts down from 5 minutes and kills the game if the user doesn't win in time.
def countdown_timer(minutes):

    global inventory
    global cryo_chamber_keypad

    start()
    cryo_pod()
    ben_final()

    os.system('clear')


    start_time = time.time()
    end_time = start_time + (minutes * 60)
    while True:
        current_time = time.time()
        if current_time >= end_time:
            os.system('clear')
            print("Mission Failure!")
            break
        else:
            time_remaining = end_time - current_time
            minutes_remaining = int(time_remaining // 60)
            seconds_remaining = int(time_remaining % 60)
            if seconds_remaining % 30 == 0: #only print the timer every 30 seconds
                print(f"Time remaining: {minutes_remaining} minutes {seconds_remaining} seconds")



            #create a loop that allows the user to type "inventory" at any time and print their inventory
            print("\nCommands: Map, Inventory, Move, Role\n")
            u_input = input("> ")
            if u_input.lower() == "inventory":
                print(f"\nTime remaining: {minutes_remaining} minutes {seconds_remaining} seconds\n")
                show_inventory()
                time.sleep(1)
            elif u_input.lower() == "role":
                print(f"\nTime remaining: {minutes_remaining} minutes {seconds_remaining} seconds\n")
                check_role()
            elif u_input.lower() == "map":
                print(f"\nTime remaining: {minutes_remaining} minutes {seconds_remaining} seconds\n")
                print("Rooms Within Ship:\n")
                map("map")
            elif u_input.lower() == "move":
                print(f"\nTime remaining: {minutes_remaining} minutes {seconds_remaining} seconds\n")
                print("Which room would you like to move to?:\n")
                map("move")
            elif u_input.lower() == "exit":
                pass

            time.sleep(1)


countdown_timer(5)

