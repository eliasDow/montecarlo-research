# calculating pi

import random
import math
import matplotlib.pyplot as plt

hits = 0
shots = 5000

xplot = [None] * shots
yplot = [None] * shots

for i in range(shots):
    shotx = random.random()
    shoty = random.random()
    r = math.sqrt(math.pow(shoty,2)+math.pow(shotx,2))
    print(r)
    if r < 1:
        hits = hits + 1
    

pi = float(4*hits)/shots

print(pi)






     