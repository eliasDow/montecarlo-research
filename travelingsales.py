# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 16:02:09 2016

@author: elias
"""
import random
import math
import numpy as np
import matplotlib.pyplot as plt

def plot(cities):
    citiesX = [None]*len(cities)
    citiesY = [None]*len(cities)
    for i in range(len(cities)-1):
        citiesX[i] = cities[i][0]
        citiesY[i] = cities[i][1]
    
    plt.plot(citiesX, citiesY, '-o')
    plt.show()


def distance(co1, co2):
    return math.sqrt((co2[0]-co1[0])**2+(co2[1]-co1[1])**2)
    
def totalDist(cityArray):
    #dist = 0
    #for i in range(len(cityArray)-1):
     #   dist = dist + distance(cityArray[i],cityArray[i+1])
    #if len(cityArray)>0:
     #   dist =  dist + distance(cityArray[len(cityArray)-1],0)
    dist1 = 0
    for cityIndex in xrange(0,len(cityArray)):
        from_city = cityArray[cityIndex]
        if(cityIndex + 1 < len(cityArray)):
            destination_city = cityArray[cityIndex+1];
        else:
            destination_city = cityArray[0];
        dist1 += distance(from_city,destination_city);
    
    return dist1
        
    
def swap(cityArray):
    #first pick 2 random indexes to swap
    index1 = random.randint(0,len(cityArray)-1)
    index2 = random.randint(0,len(cityArray)-1)
    cityArray[index1],cityArray[index2] = cityArray[index2],cityArray[index1]    
    return cityArray
    
def accept(newDist,oldDist,temp):
    if newDist<oldDist:
        #always accept
        w = 1
    if newDist>oldDist:
        w = math.exp((oldDist-newDist)/temp)
    return w
    
def anneal(solution):
    #start with start solution
    #initialize temp
    temp = 10000
    tempMin = .00001
    coolingRate = .999
    # starting distance 0
    deltaD = 0
    
    distance = totalDist(solution)
    print solution
    
    accept = 0
 
    bestVal = totalDist(solution)
    bestPath = np.array([[-1,-1]*len(solution)])
    
    while temp > tempMin:
        nextSolution = swap(solution)
        deltaD = totalDist(nextSolution) - distance
        
        # if new order has smaller distance
        # or if new order gets accepted by prob func
        if (deltaD < 0 or (distance > 0 and 
            math.exp(-deltaD/temp) > random.random)):
            accept = accept + 1
            solution = nextSolution
            if totalDist(solution)<bestVal:
                bestVal = totalDist(solution)
                bestPath = list(solution)
                #for i in range(len(bestPath)):
                 #   bestPath[i] = solution[i]
                    
            distance = deltaD + distance
        #print "best", bestVal,bestPath, totalDist(bestPath) 
        temp = temp*coolingRate
    print "accept",accept
    print "final:",bestPath
    return distance,bestPath
                    
             
        
numOfCit = 10
#array with coordinates of cities
cities = np.array([None,None]*numOfCit)
#cities = np.array([[82,44],[88,83],[39,11],[60,13],[25,64]])
#cities = [(1,5),(6,10),(3,4),(2,9)]

for i in range(len(cities)):
    cities[i] = [random.randint(10,100),random.randint(10,100)]
    print i,cities[i]
    
plot(cities)

print "start:",totalDist(cities)

final = anneal(cities)
#
#
#
print "returned running tot distance: ", final[0]
print "returned solution: ", final[1], totalDist(final[1])
plot(final[1])

