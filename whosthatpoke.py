#!/usr/bin/env pythoclen3

import os
import time

pause = 0



print("""                   
/  \    /  \  |__   ____  ______
\   \/\/   /  |  \ /  _ \/  ___/
 \        /|   Y  (  <_> )___ \ 
  \__/\  / |___|  /\____/____  >
       \/       \/           \/ """)
time.sleep(1)

print("""
 | | | |/ _ \| | | | '__|
 | |_| | (_) | |_| | |   
  \__, |\___/ \__,_|_|   
   __/ |                 
  |___/       """)

time.sleep(1)

print("""                   
    _.----.        ____         ,'  _\   ___    ___     ____
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
        \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-..|! """)

time.sleep(1)


fire = 0
water = 0
grass = 0


def questions():
    global fire
    global water
    global grass
    global poison  # all of these keywords will allow your global variables above to be edited
    

    simtype("""\n Question 1: If you could pick one vacation spot that you could go to for free, where would it be?
        \n A. Egypt   B. Fiji   C. Norway   """)
    q1 = input(">")
    q1 = q1.lower()

    simtype("""\n Question 2: If you could pick a first or additional college major from these choices, what would it be?
        \n A. Geology B. Marine Science  C. Botanical Science""")
    q2 = input(">")
    q2 = q2.lower()


    simtype("""\n Question 3: If you could choose a new hobby, or continue a favorite hobby, what would it be?
        \n A. Geocaching   B. Surfing   C.  Gardening  """)
    q3 = input(">")
    q3 = q3.lower()

    simtype("""\n Question 4: Which of these sounds like a dream home spot:
        \n A. A small Hawaiian Home near Volcano National park
        \n B. A beachfront hut on the island of the Maldives
        \n C. A serene log cabin in Casteel creek, Colorado  """)
    q4 = input(">")
    q4 = q4.lower()

    simtype("""\n Question 5: How would you describe yourself?
        \n A. Confident and headstrong
        \n B. Bubbly and outgoing
        \n C. Easygoing and go-with-the-flow""")
    q5 = input(">")
    q5 = q5.lower()

    simtype("""\n Question 6: FINAL QUESTION: What is your weakness?
        \n A. I have a hard time not being blunt
        \n B. Sometimes I procrastinate on important things
        \n C. Sometimes I don't take things seriously enough""")
    q6 = input(">")
    q6 = q6.lower()

    questions= [q1, q2, q3, q4, q5, q6]

    for question in questions:
        if question == 'a':
            fire += 1
        elif question == 'b':
            water += 1
        else:
            grass += 1

    

    if fire > grass and fire > water:
        simtype("""\nYour...pokemon...is
                ...
                ...
                ... CHARMANDER!
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠤⠤⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡠⠞⠉⠀⠀⠀⠀⠀⠈⠑⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣼⡇⠀⠀⠀⠀⠀⠀⣠⣄⠀⠈⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣸⣿⠁⠀⠀⠀⠀⠀⠀⡸⢛⣷⡀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⡿⠋⠀⠀⠀⠀⠀⠀⢰⣷⣾⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠿⢏⡏⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠋⠁⠀⡈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠘⣦⡀⠐⠂⠠⠴⠀⠀⠀⠀⠀⠀⠀⣀⡴⠀⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⢀⠀⠀⠀
⠀⢰⠦⣄⠈⢿⣶⡶⠤⠤⠤⠔⠒⠒⣶⠒⡫⢋⡄⠀⢸⠀⠀⠀⠀⢀⣀⠤⣤⠀⠀⠀⠀⠀⢀⡞⠉⠛⢆⠀⠀
⢰⡟⢷⠂⠉⠚⠿⣿⣄⣀⣀⣀⣠⣴⣛⣯⠔⠋⠀⠠⠼⠦⠔⠒⠊⠁⠠⡶⢧⡄⠀⠀⠀⠀⠸⣧⠀⡀⠈⣿⠀
⠀⠙⢮⡀⠀⠀⠀⠈⠉⡖⠛⠋⠉⠉⠁⠈⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣥⠞⠁⠀⠀⠀⠀⠀⡏⠿⢧⢀⠈⡆
⠀⠀⠀⠙⢄⠀⠀⠀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⣇⠀⠸⣯⠀⡿
⠀⠀⠀⠀⠀⠓⢄⣠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⠀⠐⠒⢖⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡀⠀⠉⣶⡇
⠀⠀⠀⠀⠀⠀⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠈⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠣⣴⢦⠞⠁
⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡎⢸⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⠸⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⣀⠜⠁⢀⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡠⠚⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠤⠤⢤⣸⠓⠢⠄⢀⠀⠤⠔⠊⠁⠀⠀⡼⠀⠀⠀
⠀⠀⠀⠀⠀⢀⠎⠀⠀⠀⠱⣄⠀⠀⠀⠀⠀⠀⠀⢀⡇⠀⠀⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡜⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡀⠀⠀⠀⠀⠈⠑⠦⣀⠀⠀⠀⣠⠞⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⢀⡠⠊⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢳⡄⠀⠀⠀⠀⠀⢀⡜⠉⠉⠛⢧⠀⠀⠀⠀⠀⠀⣸⠥⣄⣀⣀⣀⠠⠖⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣀⡴⠊⠁⠀⠀⠀⠀⠀⠀⠸⡄⠀⠀⠀⢸⠇⠀⠀⠀⢀⣴⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢿⣿⣷⣦⣀⣀⣀⡀⠤⠤⠤⠚⠁⠀⠀⠀⢸⡤⢤⡤⢤⡴⢤⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠾⡷⠞⠿⠊⠀⠀⠀""")
    if grass > fire and grass > water:
        simtype("""\nYOUR....POKEMON....IS
                ...
                ...BULBASAUR!
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠉⢳⠴⢲⠂⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠤⠤⠤⠤⠤⠤⠤⠤⠤⠖⠊⠀⣠⠎⠀⡞⢹⠏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠊⠁⠀⠀⠀⠀⠀⢀⡠⠤⠄⠀⠀⠀⠁⠀⠀⢀⠀⢸⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⠤⠤⠄⣀⠀⠀⠀⠀⢀⣌⠀⠀⠀⠀⠀⢀⣠⣆⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠘⡄⠀⠀⠀⠀
⠀⠀⠀⠀⡴⠁⠀⠀⠐⠛⠉⠁⠀⠀⣉⠉⠉⠉⠑⠒⠉⠁⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⠀⠱⡀⠀⠀⠀
⠀⠀⠀⢰⣥⠆⠀⠀⠀⣠⣴⣶⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆⠀⠑⡄⠀⠀
⠀⠀⢀⡜⠁⠀⠀⢀⠀⠻⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠀⠀⠸⡀⠀
⠀⢀⣮⢖⣧⢠⠀⣿⠇⠀⠀⠁⠀⠀⠀⠠⠀⢀⣠⣴⣤⡀⠀⠀⠀⠈⡗⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢱⠀
⠀⣼⠃⣼⣿⠘⠀⠀⠀⢠⣶⣿⡆⠀⠀⠁⣠⠊⣸⣿⣿⣿⡄⠀⠀⠀⡇⠀⢑⣄⠀⠀⠀⠀⠀⠀⢠⠃⠀⠀⠸⡆
⠀⣿⢰⣿⣿⠀⠀⠀⠀⠙⠻⠿⠁⠀⠀⠠⠁⠀⣿⣿⣿⣿⡇⠀⠀⠀⠇⠀⢻⣿⣷⣦⣀⡀⣀⠠⠋⠀⠀⠀⢀⡇
⠈⠉⠺⠿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⢿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⢦⡀⠀⠀⠀⠀⡸⠀
⠘⣟⠦⢀⠀⠀⢠⠀⠀⡠⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠁⣀⠔⠀⠀⠀⠀⠀⠀⠀⠛⠻⠟⠋⠀⠙⢦⠀⣠⠜⠀⠀
⠀⠈⠑⠤⡙⠳⣶⣦⣤⣤⣤⣤⣤⣤⣤⣤⣴⣶⡶⠞⠁⠀⠀⣠⠖⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠈⢯⠁⠀⠀⠀
⠀⠀⠀⠀⠈⢳⠤⣙⡻⠿⣿⣿⣿⣿⡿⠿⠛⠉⠀⢀⣀⡤⡚⠁⠀⠀⠀⠀⠀⠀⣧⠖⣁⣤⣦⠀⠀⠈⢇⠀⠀⠀
⠀⠀⠀⠀⠀⢸⠀⢀⣩⣍⠓⠒⣒⠒⠒⠒⠒⠊⠉⠁⢀⡟⠀⠀⣾⣷⠀⠀⠀⠀⠏⢴⣿⣿⣿⠀⠀⠀⢸⠀⠀⠀
⠀⠀⠀⠀⠀⠘⣶⣿⣿⣿⠀⠀⠈⠒⢄⣀⡀⠀⠀⠀⣼⣶⣿⡇⠈⠋⠀⠀⠀⡼⠀⠈⠻⣿⡿⠀⠀⠀⢸⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠹⡿⠿⠋⠀⠀⠀⠀⡜⠁⠈⢯⡀⢺⣿⣿⣿⠃⠀⠀⠀⢀⣼⣇⠀⠀⠀⠀⠀⠀⠀⠀⡞⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣦⣄⣠⣀⣠⠞⠀⠀⠀⠈⠛⣿⡛⠛⠁⠀⠀⠀⣠⠊⠀⠈⢦⣄⣀⣀⣀⣀⢀⡼⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠛⠉⠀⠀⠀⠀⠀⠀⠘⠛⠿⣿⠷⡾⠗⠊⠁⠀⠀⠀⠈⠉⠙⠛⠛⠛⠉⠀⠀⠀""")
    if water >= fire and water >= grass:
        simtype("""\nYOUR...POKEMON...IS
                    ...
                    ...
                    SQUIRTLE!
                    ⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡶⠞⠛⠛⠉⠉⠛⠛⠳⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⡾⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣼⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣄⠀⢹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⠃⠀⠀⣠⡖⢠⠀⠀⠀⠀⠀⠀⠀⠀⣧⣼⣷⠀⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡟⠀⠀⢠⢿⣷⣶⡇⠀⠀⠀⠀⠀⠀⠀⡿⣿⡿⠀⠘⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣇⠀⠀⢸⠸⠻⡿⠇⠀⠀⠀⠀⠀⠀⠀⠐⠒⠈⢀⠀⢹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣄⡀⣿⠀⠀⠀⠁⠀⠉⠁⢀⣀⣀⣀⣄⣤⠴⢶⣶⣿⡏⠀⣸⣃⣀⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣠⣾⠉⠛⠛⠦⠤⣄⡀⢿⡋⠉⠉⠁⠀⠀⠉⠁⠀⠀⢈⡟⢀⡼⠛⠉⠉⠉⠉⠉⠛⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⠀⠀⠀⠀⠀⠀⠀⠉⠛⢷⣦⣀⠀⣀⣠⠤⠖⠒⠒⢛⣛⣻⣷⡖⣀⡀⠀⠀⠀⠀⠀⢹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⡋⢉⣠⠴⠖⠚⠉⠉⠁⠉⠻⣍⣹⣶⣦⣀⡀⠀⠀⣸⣷⠶⠶⠶⠶⢦⣤⣴⣦⡀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⠙⠳⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣉⣀⠀⠀⠀⠀⣀⣠⠤⠖⠛⠙⢿⣄⠈⠉⠙⠻⢿⣇⠀⠀⠀⠀⢠⠟⠀⠘⠛⠻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠛⢦⣄⡀⠀⠀⠀⠀⣠⣏⡉⠉⠉⠉⢉⡿⠟⠒⠒⠤⣄⡀⠀⠉⢦⡀⠀⠀⠀⠉⢧⠀⠀⠀⠋⠀⠀⠀⠀⠀⠉⢻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠛⢷⣶⣿⣿⣭⣭⡉⠑⢦⣴⠃⠀⠀⠀⠀⠀⠀⣙⣦⣠⣄⡹⢦⣀⠀⠀⠈⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣁⣀⣠⣤⣄⣀⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣆⠘⡇⠀⠀⠀⠀⣶⠶⠞⠉⠛⠋⠘⣇⠀⠈⠳⢦⡀⠘⡆⠀⠀⠀⠀⠀⠀⠀⣰⠟⠋⠁⠀⠀⠀⠉⠙⠳⣤⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⡄⣧⠀⠀⠀⠀⣇⠀⠀⠀⠀⠀⠀⢻⠀⠀⠀⠀⠙⠳⡿⣶⣶⣤⣀⣀⣠⡴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣷⡘⢧⡀⠀⠀⢿⠀⠀⠀⠀⠀⠀⣼⠀⢀⣠⣤⣄⡼⠁⣼⠀⠀⠉⠉⣽⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣷⣤⡉⠓⠦⠼⣧⡀⠀⠀⠀⣰⡇⢠⠋⠀⠀⠀⠙⠶⣯⣀⠀⠀⠀⣿⠀⠀⠀⠀⡴⠚⠛⠳⣆⠀⠀⠀⠀⠸⣇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣶⣶⣦⣽⣶⣶⣾⣉⣉⠙⣄⠀⠀⠀⠀⠀⠈⠙⠛⠛⠛⠻⡆⠀⠀⠀⠀⠀⠀⠀⢹⡆⠀⠀⠀⠀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣄⠀⠀⠀⠀⠀⢀⡾⠀⠀⠀⠀⢰⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠿⠿⠿⠿⠛⠛⠉⠁⠀⠀⠀⠙⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⠶⢤⡤⠴⠛⠁⠀⠀⠀⢠⡿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢶⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⠶⣦⣤⣤⣀⣀⣀⣀⣠⣤⡴⠾⠋⠁⠀⠀⠀""")


def simtype(word: str):
        for i in word:
            time.sleep(pause)
            #time.sleep(0)
            print(i, end="", flush = True)

def pokedex():
    #"define starters"
    starters= [
                {'poke_id': "1",
                 'poke_name': '1. Charmander, 2. Cyndaquil, 3. Torchic, 4. Tepig',
                 'poke_type': 'Fire'
                 },


                {'poke_id': "2",
                 'poke_name': '1. Squirtle, 2. Tododile, 3. Mudkip, 4. Froakie',
                 'poke_type': 'Water'
                 },

    
                {'poke_id': "3",
                 'poke_name': '1. Bulbasaur, 2. Chikorita, 3. Turtwig, 4. Snivy',
                 'poke_type': 'Grass'
                 }
                
              ]



    simtype("""\n\nHello Trainer! I'm pokepik, the Pokemon partner chooser! 
            \nJust answer a few questions and I'll find you the perfect starter Pokemon!\n""")

    simtype("\nAre you ready? y/n ")
    start = input("> __")
    start = start.lower()



    while start not in ('y', 'yes', 'n', 'no'):
        simtype("I'm sorry that's not a valid response\n")
        simtype("Are you ready? y/n")
        start = input(" >__")

    
    if start == "y" or start == "yes":
        simtype("Ok! Lets get started!")
        questions()

    elif start == "n" or start == "no":
        simtype("Ok! I'll be back whenever you need!")



pokedex()
