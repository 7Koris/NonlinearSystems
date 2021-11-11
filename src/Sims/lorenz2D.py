import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from matplotlib import style
style.use('dark_background')

sigma = 13.727760558061053 
r = 46.7807512582482 
b = 1.7246112018548438

last_x = 1
last_y = 1
last_z = 1

x = []
y = []
z = []

xprime = []
yprime = []
zprime = []

fig = plt.figure()
ax = plt.axes()

def main():
    
    gen_lorenz()
    ani = animation.FuncAnimation(fig, animate, len(x), interval=10)
    plt.show()

def animate(i):
    ax.clear()
    xprime.append(x[i])
    yprime.append(y[i])
    zprime.append(z[i])
    ax.plot(xprime, yprime, color='white')
    ax.plot(x[i], y[i], markerfacecolor='r', markeredgecolor='r', marker='.', markersize=10, alpha=0.6)

def gen_lorenz():
    global last_x
    global last_y
    global last_z
    global x
    global y
    global z

    iteration = 0
    while iteration < 500:
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