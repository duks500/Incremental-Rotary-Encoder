from velocity import *
from plotTOfile import plotONGraph, x_smooth, y_smooth, marker_on, listOfTotalTimeArray, listOfVeclocityArray

import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from matplotlib import style


style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    graph_data = open ('plottPoint.txt','r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    plotONGraph()
    ax1.clear()
    ax1.plot(x_smooth, y_smooth, '-gD', markevery = marker_on)


ani = animation.FuncAnimation(fig, animate, interval = 100)
plt.show()
