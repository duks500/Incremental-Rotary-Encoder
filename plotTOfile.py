import matplotlib.pyplot as plt 

plottPoint = open('plottPoint.txt','r') #open the file

contentTXT = 0 #the new list

totalSecond = 0 #total number of seconds
listOfVeclocity = [] #list of all the diffrence between A and B


listOfTotalTime = [] #list of total timw

### read the text file and save it into a new list ###
def saveThePointIntoList():
    global plottPoint, contentTXT #dlobal variable
    contentTXT = plottPoint.read().splitlines() #read the file and save it into contentTXT
    plottPoint.close() #close the file

    ## remove the extra space between lines ##
    while("" in contentTXT) : 
        contentTXT.remove("")

    for x in range(len(contentTXT)):
        listOfVeclocity.append(contentTXT[x])


### total time in seconds and save it tinot a list increment every 100 millisecnd###
def totalTime():
    saveThePointIntoList()
    global listOfTotalTime #global variable

    for x in range(len(contentTXT)):
        listOfTotalTime.append(x)

    

### plot x as total second and y as velocity ###
def plotONGraph():
    totalTime() #calculate the total time and save the points

    global totalSecond, contentTXT #global variable

    plt.plot(listOfTotalTime,listOfVeclocity) #plot on the graph

    plt.xlabel('x - axis') # naming the x axis 
    plt.ylabel('y - axis') # naming the y axis 
    plt.title('My first graph!') # giving a title to my graph 
    plt.show() # function to show the plot 



plotONGraph()
