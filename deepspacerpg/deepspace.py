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
#cryo chamber opens to cryo unit. Alarms sound - user must find their way out
    #in cryo chamber is oxygen suit, keypad, and large table
    #options for user input - take suit, walk to keypad, walk to table
    #note taped to table - numbers - read numbers
    #large bang at the cryo chamber door
#steps into hallway - lights flicker - options to go left or right
