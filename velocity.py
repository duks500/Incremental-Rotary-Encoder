content = 0

deltaA = 0 #first distance
deltaB = 0 #second distance
velocityAandB = 0 #the diffrence between A and B
listOfVeclocity = [] #list of all the diffrence between A and B
firstTime = True #check for if it is the first time running

lastElement = 0 #last element in the list
totalSecond = 0 #total number of seconds

plottPoint = open('plottPoint.txt','w') #current velocity
plottPointest = open('plottPointest.txt','w')


listOfTIME = [] #list of time at every level

### a method to print out the text file ###
def clearText():
    newTxtFile = open('distance_between.txt','r') #open the file
    global content #declar global veriable
    content = newTxtFile.read().splitlines() # save the input from the file into a list sepereated by new line
    newTxtFile.close() #close the file

    ## remove the extra space between lines ##
    while("" in content) : 
        content.remove("")
    
    ## converting the list into float ##
    for x in range(len(content)):
        content[x] = float(content[x])
    
    #print("The original list is : " + str(content)) #print out the results


### a method to calculate the diffrence in between deltaA and deltaB and for the current velocity in mm/second###
def calculateVel():
    global firstTime, deltaA, deltaB, velocityAandB #declar global veriable

    ## a for loop to first check if this is the first time running and save virables to deltaA and deltaB ##
    for x in range(len(content)):
        if(firstTime == True):
            deltaA = content[x]
            firstTime = False
        else:
            deltaB = content[x]
        
        dltaAandB = deltaB - deltaA #calculate the diffrence between deltaA and deltaB = distance
        velocityAandB = round(float(dltaAandB / 2), 4) #divide the diffrence between deltaA and deltaB by the total time in seconds to recive the velocity
        listOfVeclocity.append(velocityAandB) #save the value of the velocity into a list
        deltaA = deltaB #making deltaA to equal to deltaB for the next loop
        print(str(velocityAandB)) #print the list

        printVelocity(velocityAandB) #save the value into a text file


### a method to calculate the total average velocity in mm/ds (1 ds = 100 millisecond = 0.1 second) ###
def averageVelcoticy(lis):
    sum = 0 #set a sum variable

    ## a for loop to simple add all of the list into the sum variable ##
    for ele in lis: 
        sum += ele
    
    res = sum / len(lis) #calculate the results by taking the total sum and divide it by the total lenth
    return res #return the average


### a method to print the last element in the orifinal list = total distance in ###
def totalDistance(lis):
    global lastElement
    lastElement = lis.pop() * 10 #pop the last element, convert it to cm
    print (lastElement)


### total time in seconds ###
def totalTime(lis):
    global totalSecond
    totalSecond = len(lis) /10


### a method to print the current volicity into a text file ####
def printVelocity(vel):
    global plottPoint

    # plottPoint.write(round(float(vel), 4))
    if(float(vel) > 0):
        plottPoint.write(str(vel))
        plottPoint.write('\n')
    else:
        plottPoint.write('0')
        plottPoint.write('\n')


### a method to calculate the total valecotiy ###
def totalVelocity():
    global plottPointest, listOfVeclocity
    sum = 0
    time = 0

    ## a for loop to simple print the total value at each time ##
    for ele in range(len(listOfVeclocity)): 
        time += ele
        sum += listOfVeclocity[ele]
        plottPointest.write(str(sum))
        plottPointest.write('\n')
        #print(time, sum)




clearText() #needs to be first
calculateVel() #needs to be second
averageVel = averageVelcoticy(listOfVeclocity) #save the total average velocity
totalTime(listOfVeclocity) #check for total time


totalDistance(content)

totalVelocity()


