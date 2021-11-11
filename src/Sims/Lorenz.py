import matplotlib.pyplot as plt
import matplotlib.pylab as pl
import numpy as np
from matplotlib import style
import random as rand
style.use('dark_background')

sigma = rand.random() * rand.randrange(0, 100)
r = rand.random() * rand.randrange(0, 100)
b = rand.random() * rand.randrange(0, 100) + 0.1
print(sigma, r, b)

last_x = 1
last_y = 1
last_z = 1

x = []
y = []
z = []

fig = plt.figure()

ax = plt.axes(projection='3d')


def main():
    global sigma
    global r
    global b
    global last_x
    global last_y
    global last_z
    global x
    global y
    global z


    n = 1 #The number of attractors to generate
    colors = pl.cm.jet(np.linspace(0,1,n))

    

    for i in range(0, n):
        sigma = 27.390669540590586 

        r = 16.024814219194866 

        b = 1.7540526438099215

        gen_lorenz()
        last_x = 0.1
        last_y = 0.1
        last_z = 0.1
        ax.plot3D(x, y, z, color=colors[i])
        
        x = []
        y = []
        z = []

    

    plt.show()

def gen_lorenz():
    global last_x
    global last_y
    global last_z
    global x
    global y
    global z

    iteration = 0
    while iteration < 5000:
        x.append(last_x)
        y.append(last_y)
        z.append(last_z)

        newx = last_x
        newy = last_y
        newz = last_z

        newx += (sigma*(last_y-last_x)) * 0.01
        
        newy+= ((r*last_x)-last_y-(last_x*last_z)) * 0.01
        
        newz+= ((last_x*last_y)-(b*last_z)) * 0.01

        last_x = newx
        last_y = newy
        last_z = newz

        iteration += 0.01
main()