#! /usr/bin/env python3

"""Welcome to Deep Space! You are an Astronaut aboard an interstellar craft.
You awake from cryo-sleep with almost no knowledge of how long you've been asleep.
You're job is to find your crew, fix your ship, and reset your navigation system back on course; but, 
be weary, something is amiss aboard your spacecraft..."""

#import dstitle.py
import os
import sys
import time

pause = .065

import dstitle
import dschoices


#typing effect
def simtype(word: str):
    for i in word:
        time.sleep(pause)                                                                                                   
        #time.sleep(0)
        print(i, end="", flush = True)

#take user input male or female and name
simtype("Cosmonaut........wake up cosmonaut... ...")
simtype("\nOh good...you're awake")

time.sleep(1)


print('-')
print("\n\n\x1B[3mYou awaken inside a pod-like chamber, lights are flashing and the feint sound of an alarm is going off in the distance\x1B\n\n")
print('-')


#add sprite

#sprite name - B.E.N. - Bio Electronic Navigator



"""this will act as the primary source for user choices"""

#back of ship contains 4 rooms. Each with own tasks
back_of_ship = {
    "cryochamber":
    {"table": "unread note", #must read note to unlock keypad
        "suit": "untaken",   #take suit to identify name and rank
        "keypad": "locked"}, #keypad unlocks with code on note

    "agbay":
    {"scienceofficerkey": "left", #turn to taken when 'pickup'
        "docsnotes": "unread",    #read docs notes for story
        "oxygensuit": "untaken", #must have for docking
        "journal": "unread"},    #ACHEIVEMENT

    "dockingbay":
    {"pressurizationpad": "locked", #must have oxysuit
        "door": "locked"},          #must have mission spec key

    "engineroom":
    {"door": "locked", #key is in flight engineer room
        "wires": "split"}, #combination is in flightengineer room


#the central corridor of the ship has 3 rooms on each side with the end pointing to the flight deck.

#first section of middle corridor 
#mission specialist LEFT flight enginner RIGHT
midship_one = {
    "missionspecroom":
    {"door": "locked",   #have to take vent, open when leaving
    "vent": "closed",   #open
    "key" : "left",     #key to docking bay
    "notes": "unread",  #notes detailing pressure pad
    "journal": "unread"}, # ACHEIVEMENT

    "flightengineer":
    {"sticky": "unread", #sticky has clue to safe combo
        "safe": "locked",#safe combo unlocks
        "notes": "not taken"}, #notes need to be had for wires


#central corridor section 2
#doctor cosmonaut LEFT science officer RIGHT





#ben takes user input
simtype("""\nCosmonaut, my name is B.E.N. I am the Bio-Electronic Navigator of this craft. My systems indicate multiple malfunctioning components as well as a course-divergence of...
    ...
    calculating
    ...
    113 light years
    At this rate, it will take approximately...
    ...
    1,130 years to adjust course. Unfortunately, bio sensors indicate no other crewmmates """)

#begin first task - break out of cryo-chamber
def cryo():
    simtype("Good job, cosmonaut. We are now in the crychamber. We have to make it to the Flight deck in order to reroute the course.")
    print("\n\n\x1B[3mYou step out of the crypod into a room. A red light rotates above a steel door to your left. Alarms can still be heard in the distance. Directly to the left and right of your crypod are the pods of your crewmates. In front of you is a table, and on the other side are a row of hanging suits \x1B\n\n")
    if task == "table":
        print("You have chosen the task: table.")
    elif task == "suit":
        print("You have chosen the task: suit.")
    elif task == "number lock":
        print("You have chosen the task: number lock.")
    else:
        print("Invalid task choice.")




#cryo chamber opens to cryo unit. Alarms sound - user must find their way out
    #in cryo chamber is oxygen suit, keypad, and large table
    #options for user input - take suit, walk to keypad, walk to table
    #note taped to table - numbers - read numbers
    #large bang at the cryo chamber door
#steps into hallway - lights flicker - options to go left or right
