# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 11:42:11 2021

@author: john
"""
import numpy as np

WDCIntervals = [256.5, 433.5, 696, 831, 976, 1071, 1187.5, 1303.5, 1361.5, 1407.5, 1481.5, 1499.5, 1534.5, 1560.5, 1576.5, 1583.5, 1589.5, 1591.5, 1592.5, 1593.5]

WCCOrder = [433.5, 397.5, 240, 232.5, 104, 92, 61, 23, 8, 2]

WDCLookup = ['Hamilton', 'Bottas', 'Verstappen', 'Perez', 'Norris', 'Ricciardo', 'Sainz', 'Leclerc', 'Alonso', 'Ocon', 'Gasly', 'Tsunoda', 'Vettel', 'Stroll', 'Russell', 'Latifi', 'Raikkonen', 'Giovinazzi', 'Schumacher', 'Mazepin']

RaceLookup = ['Bahrain', 'Imola', 'Portugal', 'Spain', 'Monaco', 'Azerbaijan', 'France', 'Steiermark', 'Austria', 'Silverstone', 'Hungary', 'Belgium', 'Netherlands', 'Italy', 'Russia', 'Turkey']

Points = ['25 pts', '18 pts', '15 pts', '12 pts', '10 pts', '8 pts', '6 pts', '4 pts', '2 pts', '1 pt']

def get_total(inputlist):
    c = 0
    for i in range(len(inputlist)):
        c += inputlist[i]
    return c

def run_race(constructors, drivers):
    result = [None] * 10
    selected_drivers = { }
    current_driver = None
    i = 0
    while i < len(result):
        randvar = np.random.randint(0, get_total(constructors) + 1)
        for j in range(len(drivers)):
            if drivers[j] - randvar >= 0:
                current_driver = WDCLookup[j]
                break
        if selected_drivers == { }:
            selected_drivers[current_driver] = "added"
            result[i] = current_driver
            i += 1
            continue
        else:
            if current_driver not in selected_drivers.keys():
                selected_drivers[current_driver] = "added"
                result[i] = current_driver
                i += 1 
                continue
            else:
                continue
    
    return result


def run_season():
    results = [run_race(WCCOrder, WDCIntervals) for i in range(len(RaceLookup))]
    for i in range(len(results)):
        print(RaceLookup[i] + " Grand Prix:" + "\n")
        for j in range(len(results[i])):
            print("P" + str(j + 1) + ": " + results[i][j] + ", " + Points[j] + "\n")
        print("\n")

print(run_season())