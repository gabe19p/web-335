
# Title: purselley_hobbies.py
# Author: Danial Purselley
# Date: 6 Sep 2022
# Description: demonstrating 
# loops with python

import random

# list of hobbies
hobbies = ["Golf", "Photography", "Gaming", "Drawing", "Grilling"]
# loop through the hobbies
for i in hobbies:
    print(i)

# list of days
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
# loop through the days
for day in days:
    # randomize my hobbies list for the weekend
    randomHobby = random.choice(hobbies)
    # if statements for the days in the week
    if(day != "Saturday" and day != "Sunday"): print("Its " + day + ", I'll be at work today!")
    # weekend output
    else: print("Its " + day + ", take a day off work and enjoy some " + randomHobby)
