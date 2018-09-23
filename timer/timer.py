#!/usr/bin/python3.6

# Enhancements:
#  - save favorite times to config file
#  - allow input for seconds
#  - use some kind of curses type library to make display nicer
#  - make a sound on stop

from os import system
import time

def get_minutes_input():
    minutes = input("How many minutes? > ")
    minutes = int(minutes)
    return minutes

def generate_times(minutes):
    times = []

    minute = minutes
    second = 0
    times.append( "{:02} : {:02}\n".format(minute, second) )

    for minute in range(minutes-1, -1, -1):
        for second in range(59, -1, -1):
            time_entry = "{:02} : {:02}\n".format(minute, second)
            times.append(time_entry)

    return times

def timer(times):
    for time_entry in times:
        system("clear")
        system(f"figlet {time_entry}")
        time.sleep(1)

    system("clear")
    system("figlet STOP!")


input_minutes = get_minutes_input()
times = generate_times(input_minutes)
timer(times)
