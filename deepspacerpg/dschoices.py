#! /usr/bin/env python3


#this will act as the primary source for user choices in deepspace

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


            

