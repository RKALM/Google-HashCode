#################################
#LIBRARIES(START)
#################################

from __future__ import division
import math
import random
#import numpy

#import sys
#import os
#import datetime

##############
#LIBRARIES(END)
##############




#########################
#GLOBAL VARIABBLES(START)
#########################
itIsTheFirstLine = True     #This variable is about the input line. If the line is the first the variable itIsTheFirstLine is True.
itIsTheSecondLine = True
T=0     #The number of lines with usefull Data. the number of tierations.
result = "Not any result right now" #this is used for the result wich is printed in the end of the code with the default value.
testSum = 0 #This is used to make the mainCheckFunction() bit more interesting but making the function to work as add function.
countForT = 0 #this is the count vairiable that helps to check that the iterations are not more than the predefined T variable.
i = 0
countForDwnldN = 0
dwnldK = 0
dwnldTArray = []
dwnldDarray = []
spliterFunctionsArray = []
videoArrayX = []
videoArray = []
endPointArray = []
requestArray = []
#first line variables.
howManyVideos = 0
howManyEndPoints = 0
howManyRequests = 0
howManyCaches = 0
howManyMBsPerCache = 0

fileForOutput = open('output.txt','w')
fileForInput = open('input.in','r')
#######################
#OGLOBAL VARIABLES(END)
#######################



##########################
#TEMPLATE FUNCTIONS(START)
##########################


def loader():
    global countForT, i
    for N in fileForInput:
        print("itIsTheFirstLine now is " + str(itIsTheFirstLine))
        fileForOutput.write("itIsTheFirstLine now is " + str(itIsTheFirstLine))
        #print("itIsTheFirstLine now is " + str(itIsTheFirstLine) end='\n' file=f)
        if itIsTheFirstLine == True:
            firstLineCorrection(N.rstrip('\n'))
            firstLineSpliter(N.rstrip('\n'))
        elif itIsTheSecondLine == True:
            SecondLineCorrection()
            secondLineSpliter(N.rstrip('\n'))
            videoArrayRepairer()
        else:
            if int(i) <= int(howManyEndPoints):
                endPointHandler(N.rstrip('\n'), i)
                endPointReapairer(howManyEndPoints)
            else:
                requestArrayCollector(N.rstrip('\n'))
                requestArrayReapairer(howManyRequests)

def printTheResults():
    print("howManyVideos variable is " + str(howManyVideos))
    print("howManyEndPoints variable is " + str(howManyEndPoints))
    print("howManyCaches variable is " + str(howManyCaches))
    print("howManyVideos variable is " + str(howManyVideos))
    print("howManyMBsPerCache variable is " + str(howManyMBsPerCache))
    print("videoArray list has " + str(videoArray))
    print("endPointArray list has " + str(endPointArray))
    print("requestArray list has " + str(requestArray))



#the mainCheckFunction() function is doing the necessary checking before the mainCalculativFunction().
#there is always something to check
def mainCheckFunction(checkFunctionsProperty):
        if checkFunctionsProperty == True:
                return True

#The function mainCalculativFunction() solves the logical problem of the exercise.
#Now it works like a SUM function.       
def mainCalculativFunction(inputProperty):
    global testSum #This is used to make the mainCheckFunction() bit more interesting but making it to work as add function.
    if mainCheckFunction(True):
        testSum = int(inputProperty) + testSum
        return str(testSum) 

#The function firstLineCorrection() changes the itIsTheFirstLine to False and stores the N to the variable T
def firstLineCorrection(inputForNInitiation):
    global itIsTheFirstLine
    global T
    itIsTheFirstLine = False
    T = inputForNInitiation


def SecondLineCorrection():
    global itIsTheSecondLine
    itIsTheSecondLine = False


# this is the function that uses the countForT to check up that the iterations are not more than what the T variable defines
def iterationsCheck(hereGoesTheCountForTParameter):
    if hereGoesTheCountForTParameter >= int(T):
        return True


# My first thought was to use "for in" loop but after using it I figured out that the use of Range is the best solution.
# As I know, a loop with range is more efficient than the typical "for in" loop.
# Use this function in case of sorting, or in the case of temparated array. you will not regret it.
def printFromArray(Arrayname, probablytheTVariable):
    for i in range(int(probablytheTVariable)):
        print(str(Arrayname[i]))


def printFromArray2(Arrayname):
    for i in Arrayname:
        print(str(Arrayname[i]))


# fills a two-dimensional array with the value N, (the line from the input).
# it needs to get called for every line from the main iteration, (for every N)
# it needs to work before the twoDimentionalArrayHandler()
# it works optimaly inside the mainCalculativFunction()
def spliterFunction(strValueFromN):
    global spliterFunctionsArray
    spliterFunctionsArray.append(strValueFromN.split(' '))


# this is the best way to handle the second dimention of two dimentional array
# it needs to work after the spliterFunction()
# it works optimaly inside the mainCalculativFunction()
# initialy works as sum function
def twoDimentionalArrayHandler(arrayNameParameter, Iterationsnumber):
    return int(arrayNameParameter[Iterationsnumber][0]) + int(arrayNameParameter[Iterationsnumber][1])


def firstLineSpliter(inputFromN):
    global howManyVideos, howManyEndPoints, howManyRequests, howManyCaches, howManyMBsPerCache
    firtstLine = inputFromN.split()
    howManyVideos = firtstLine[0]
    howManyEndPoints = firtstLine[1]
    howManyRequests = firtstLine[2]
    howManyCaches = firtstLine[3]
    howManyMBsPerCache = firtstLine[4]


# this function splits the second line.
# it inserts the content of the second line to videoArrayX
def secondLineSpliter(inputFromN):
    videoArrayX.append(inputFromN.split())


# videoArrayX is a buggy array so we need to run videoArrayRepairer() to fix it.
def videoArrayRepairer():
    for i in videoArrayX[0]:
        videoArray.append(i)


# this is a very importan function and it will help me to create the function caser()
# it vreaks the stream to separated cases.
# it took me a while to implement it.
def endPointHandler(inputFromN, inputForI):
    global countForDwnldN, latency, endPointArray, i
    i = inputForI
    # endPointArray = []*int(howManyEndPoints)
    print("endpointHandler started")
    print("i now is " + str(i))
    endpointvalues = ""
    endpointvalues = inputFromN.split()
    if int(countForDwnldN) == 0:
        print("countForDwnldN is 0")
        print("endpointvalues is " + str(endpointvalues))
        latency = endpointvalues[0]
        print("latency is " + str(latency))
        countForDwnldN = endpointvalues[1]
        print("countForDwnldN is " + str(countForDwnldN))
        i = int(i) + 1
        endPointArray.append([])
        endPointArray[i - 1].append(latency)
    else:
        print("countForDwnldN is NOT 0")
        print("countForDwnldN is " + str(countForDwnldN))
        print("i is " + str(i))
        endPointArray[i - 1].append(endpointvalues)
        countForDwnldN = int(countForDwnldN) - 1
        print("endPointArray is " + str(endPointArray[i - 1]))
        # i = int(i) + 1


# it needs to run after the endPointHandler()
# it repairs if necessary the endPointArray
# it repairs endPointArray by removing the empty trailer.
def endPointReapairer(howManyEndPointsParameter):
    if len(endPointArray) > int(howManyEndPointsParameter):
        endPointArray.pop()


# it collects the videorequests from the stream
# it fills the requestArray with the requests
def requestArrayCollector(inputFromN):
    requestArray.append(inputFromN.split(' '))


# it needs to run after the requestArrayCollector()
# it repairs if necessary the requestArray
# it repairs requestArray by removing the empty trailer.
def requestArrayReapairer(howManyRequestsParameter):
    if len(requestArray) > int(howManyRequestsParameter):
        requestArray.pop()


# attended for the caser() function.
# Not useful yet
def insideCaseCalculation(dwnldNparam, dwnldKparam):
    pass

##########################
#TEMPLATE FUNCTIONS(END)
##########################
        
        
#################################
#OBJECT ORIENTED FUNCTIONS(START)
#################################
#stuff that help objects to do stuff.
#Those function are meant to be only inside the mainCalculativFunction()


#Helper function to calculate distance between 2 points
def distance(p1, q1, p2, q2):
    return math.sqrt((p1-q1)**2 + (p2-q2)**2)

#################################
#OBJECT ORIENTED FUNCTIONS(END)
#################################


###############
#CLASSES(START)
###############
#Here are all the classes.


#############
#CLASSES(END)
#############

class Object:
    def __init__(self):
        print("I am an object and i just been constructed")
        
class Cote(object):
    def __init__(self):
        print("I am an cote and i just been constructed")
        
class Chicken(Cote):
    def __init__(self):
        print("Winner! Winner! Chicken dinner!")
        
class Egg(Cote):
    def __init__(self):
        print("Hello sir! I am an egg and the answer for everything is 42")


#######################
# MAIN() FUNCTION(START)
#######################

# The main iteration, (AKA the main loop), now is the main() function.
# The separation of code to functions blocks keeps the template simple and clear.
def main():
    countForT
    loader()
    printTheResults()


if __name__ == "__main__": main()

#####################
# MAIN() FUNCTION(END)
#####################



#Optimal print example
#print("Case #", str(unregisteredcase), ": ", number_string2, " ",sep="", end='\n', file=f)


fileForInput.close()
fileForOutput.close()
print("That's all folks!")

