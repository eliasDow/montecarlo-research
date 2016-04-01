#if random < .4999 step left
# if random > .5 step right
import random

import matplotlib.pyplot as plt



steps = 20

walkers = 100000

location = 0
result  = [None] * walkers

#Change this number in order to change # of walkers
while walkers>0:
    

    for index in range(steps):
        ranNum = random.random()
        if ranNum < .4999:
            location= location - 1
        else:
            location= location + 1
    
    
    result[walkers-1] = location
    walkers= walkers - 1
   # print(result)
    location = 0
    
    

#print(result)    

plt.hist(result)
plt.xlabel("location")
plt.ylabel("frequency")

fig = plt.gcf()
plt.show()    
        
                
    
        
        
