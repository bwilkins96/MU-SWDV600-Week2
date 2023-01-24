# A program to calculate the amount of filler needed for bowling balls
# using the number of balls, the diameter of each ball, and the volume of a core in each ball

import math

def main():
    num_balls = int(input('How many bowling balls will be manufactured? '))
    radius = float(input('What is the diameter of each ball in inches? ')) / 2
    core_volume = float(input('What is the core volume in inches cubed? '))

    volume = ((4/3) * math.pi * radius**3) - core_volume
    filler_needed = volume * num_balls

    print(f'\nYou will need {filler_needed} inches cubed of filler')

main()