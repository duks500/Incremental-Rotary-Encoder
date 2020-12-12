import matplotlib.pyplot as plt 
from scipy.interpolate import make_interp_spline, BSpline
import numpy as np


plottPoint = open('plottPoint.txt','r') #open the file

contentTXT = 0 #the new list

totalSecond = 0 #total number of seconds
listOfVeclocity = [] #list of all the diffrence between A and B
listOfVeclocityArray =[] #list of all the diffrence between A and B Array


listOfTotalTime = [] #list of total time
listOfTotalTimeArray = [] #list of total time Array


### read the text file and save it into a new list and than into an array###
def saveThePointIntoList():
    global plottPoint, contentTXT, listOfVeclocityArray #dlobal variable
    contentTXT = plottPoint.read().splitlines() #read the file and save it into contentTXT
    plottPoint.close() #close the file

    ## remove the extra space between lines ##
    while("" in contentTXT) : 
        contentTXT.remove("")

    for x in range(len(contentTXT)):
        listOfVeclocity.append(contentTXT[x])
        listOfVeclocityArray = np.array(listOfVeclocity)


### total time in seconds and save it tinot a list increment every 100 millisecnd than saved into an Array###
def totalTime():
    saveThePointIntoList()
    global listOfTotalTime, listOfTotalTimeArray #global variable

    for x in range(len(contentTXT)):
        listOfTotalTime.append(x)
        listOfTotalTimeArray = np.array(listOfTotalTime)

    

### plot x as total second and y as velocity ###
def plotONGraph():
    totalTime() #calculate the total time and save the points

    global totalSecond, contentTXT, listOfTotalTimeArray, listOfVeclocityArray #global variable
    #plt.plot(listOfTotalTime,listOfVeclocity) #plot on the graph

    ##test##
    x_smooth = np.linspace(listOfTotalTimeArray.min(), listOfTotalTimeArray.max(), len(listOfVeclocity))
    spl = make_interp_spline(listOfTotalTimeArray, listOfVeclocityArray, k=1)
    y_smooth = spl(x_smooth)
    for x in range(len(y_smooth)):
        print(x_smooth[x],y_smooth[x], listOfVeclocityArray[x])

    plt.plot(x_smooth, y_smooth)
    ##end##


    plt.xlabel('x - Time') # naming the x axis 
    plt.ylabel('y - Velocity') # naming the y axis 
    plt.title('Speed Test!') # giving a title to my graph 
    plt.show() # function to show the plot 


plotONGraph()
