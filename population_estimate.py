# A function that predicts future population size
from math import e

def population_estimate(initial, growth_rate, years):
    future = initial * e**(growth_rate * years)
    return int(future)

#print(population_estimate(10000, .4, 5)) # 73,890