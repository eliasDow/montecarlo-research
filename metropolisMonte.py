# ratio of probability of accepting move:
# e^(-Unm/kT)  where U is the mass of the atom
# k is a constant
# T is temp


#==============================================================================
# V(r) = De * ( exp[-2 * a * (r - re)] - 2 * exp[-a * (r - re)] )
# 
# Each system will have its own unique values of De, a, and re; for the argon dimer, these are:
# De = 142.9 kB * K 
# a = 1.691 Å^-1
# re = 3.762 Å
# 
# kB is the Boltzmann constant
# K is kelvin
# Å is angstrom (10^-10 m)
#==============================================================================

import random
import math
from scipy import constants
import matplotlib.pyplot as plt




particles = 100

k = constants.k
T = 300 # temperature
U = 0 # mass 
a = .00000001       # width
x = 0           # position
re = 3.762      # equilibrium bond distance

#y = 1

#calculate start energy here
U = .5*a*math.pow(x,2) # .5*a*x^2 = potential

maxDis = .000001
accept = 0
count=0

sumTotal = 0


for i in range(particles):
    sumTotal = sumTotal + monte(a,k,U,maxDis)
            
    
            
            
print "SUM: ",sumTotal
print "ACCEPT: ",(float(accept) /particles)
print "IDEAL AVG ENERGY: ", float(.5)*k*T


def monte(a,k,U, maxDis):
    disX = (random.random() - .5)*maxDis #where max is max displacement
    
    
    #disY = (random.random() - .5)*maxDis
    #disZ = (random.random() - .5)*max
    x = float(x) - float(disX)
    print "disX: ", disX
    print "x:  ", x
    #y = y - disY
    
    #gets deltaU
    print "U: ", U
    deltaU = U -.5*a*math.pow(x,2)
    
    print "deltaU: ",deltaU
    
    if deltaU < 0:
        print("NEG = accepted")
        accept = accept +1
        sumTotal = sumTotal+deltaU
        U = U - deltaU
    else:
        randAcc = random.random()
        w = math.e** (- float(deltaU) / (k*T))
        print "rand: ",randAcc,"||| w:",w
        if w > randAcc:
            accept = accept+1
            sumTotal = sumTotal+deltaU
            U = U - deltaU
        else:
            print("keep old")
            
    return U
            
