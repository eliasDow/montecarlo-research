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


particles = 1000

loop = 0;

while loop<1000:
    
    k = 1
    eps = 1
    sigma = 1
    T = 300 # temperature
    x = 0           # starting position
    r = 1.5   # equilibrium bond distance
        
    #calculate start energy here
    U = float(4)*(r**-12-r**-6) # 4(r^-12-r^-6) = potential
    
    maxDis = 10
    accept = 0
    count=0
    
    sumTotal = 0
    
 
    loop = loop+1

    for i in range(particles):
        
        disX = (random.random() - .5)*maxDis #where max is max displacement
        
        x = float(x) - float(disX)  #gets new x
        #print "disX: ", disX
        #print "x:  ", x
        #y = y - disY
    
        #gets deltaU
        #print "U: ", U
        deltaU = U -float(4)*(r**-12-r**-6)
        U = float(4)*(r**-12-r**-6)
        
        #print "deltaU: ",deltaU
        
        if U < 0:
            #print("NEG = accepted")
            accept = accept +1
            sumTotal = sumTotal+U
            
        else:
            randAcc = random.random()
            w = math.e** (-float(deltaU)/(k*T))
            #print "rand: "randAcc,"||| w:",w
            if w > randAcc:
                accept = accept+1
                sumTotal = sumTotal+U
                U = U - deltaU
            
        

            
    
print "SUM: ",sumTotal/particles
print "ACCEPT %: ",(float(accept) /particles)
print "IDEAL AVG ENERGY: ", float(.5)*k*T


            
