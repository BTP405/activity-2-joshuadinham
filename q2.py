from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys

filename = sys.argv[1]

def graphSnowfall(t):
    """read numbers from a file and graph the number of occurrences within each range as a bar graph """
    numbers = []
    with open(t) as numberFile:
        for line in numberFile:
            numbers.append(int(line.strip()))

    print(numbers)
    sorted_numbers = sorted(numbers)
    print(sorted_numbers)
    #create dictionary with ranges as the x value, and occurrences as y value
    snow_fall_ranges = {"0-10cm":0, "11-20cm":0, "21-30cm":0, "31-40cm":0, "41-50cm":0, "51-60cm":0, "60+":0}
    
    snow_fall_keys = list(snow_fall_ranges)

    #for each number in sorted numbers list
        #find the index by using the floor function -1 to account for 11/21/31 ect
        #increment the dictionary value at the key by using the index to find the key name from the list of keys
    for number in sorted_numbers: 
        index = (number - 1) // 10
        snow_fall_ranges[snow_fall_keys[index]] += 1

    print(snow_fall_ranges)

    #plot the bar graph
        #range is the amount of keys, names are the key values
        #the ticks for x increment are the key of the dictionary as well
    plt.bar(range(len(snow_fall_ranges)), snow_fall_ranges.values(), align='center')
    plt.xticks(range(len(snow_fall_ranges)), list(snow_fall_ranges))
    plt.show()

graphSnowfall(filename)

