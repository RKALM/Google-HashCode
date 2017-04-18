#!/usr/bin/env python
# -*- coding: utf-8 -*-

#################################
#LIBRARIES(START)
#################################
from __future__ import division
import math
import random
import numpy as np
import quarkball.fill_caching as f_caching
import quarkball.utils  as util
import quarkball.test_utils  as test_u
import quarkball.__init__ as init

#import sys
#import os
#import datetime

##############
#LIBRARIES(END)
##############

################
#METADATA(START)
################
# :: Project Details
INFO = {
    'authors': (
        'Robert Alm <robertkristianalm@gmail.com>',
    ),
    'copyright': 'none for now',
    'license': 'GNU General Public License version 3 or later (GPLv3+)',
    'notice':
        """
This program is free software and it comes with ABSOLUTELY NO WARRANTY.
It is covered by the GNU General Public License version 3 (GPLv3).
You are welcome to redistribute it under its terms and conditions.
        """
}

##############
#METADATA(END)
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



######################
#MODULE CALLERS(START)
######################

#Here is the place that all function callers
#for other modules are collected.

def initPyNotAnActualFunction():
    #module __init__.py is accessed as init
    init.msg()
    #Display a feedback message to the standard output.
    """
        Display a feedback message to the standard output.

        Args:
            text (str|Any): Message to display or object with `__repr__`.
            verb_lvl (int): Current level of verbosity.
            verb_threshold (int): Threshold level of verbosity.
            fmt (str): Format of the message (if `blessed` supported).
                If None, a standard formatting is used.
            *args (tuple): Positional arguments to be passed to `print`.
            **kwargs (dict): Keyword arguments to be passed to `print`.

        Returns:
            None.

        Examples:
            >>> s = 'Hello World!'
            >>> msg(s)
            Hello World!
            >>> msg(s, VERB_LVL['medium'], VERB_LVL['low'])
            Hello World!
            >>> msg(s, VERB_LVL['low'], VERB_LVL['medium'])  # no output
            >>> msg(s, fmt='{t.green}')  # if ANSI Terminal, green text
            Hello World!
            >>> msg('   :  a b c', fmt='{t.red}{}')  # if ANSI Terminal, red text
               :  a b c
            >>> msg(' : a b c', fmt='cyan')  # if ANSI Terminal, cyan text
             : a b c
        """

    init.my_actual_code()
    #parameters (*args, **kwargs)
    # it has a "TO DO" to modify

    init.handle_arg()
    #Handle command-line application arguments.
    # :: Create Argument Parser

    init.main()
    # :: handle program parameters


def fill_cachingPyNotAnActualFunction():
    #module fill_caching.py is accessed as f_caching
    #it is a collection of caching classes that inherit from Caching class
    #chaching class comes from utils module

    #The class is the f_caching.CachingRandom(Caching)
    f_caching.CachingRandom.fill()
    #parameters(self, network)


    #The class is the f_caching.CachingRandomSeed(Caching)
    f_caching.CachingRandomSeed.fill()
    #parameters(self, network)


    #The class is the f_caching.CachingOptimByRequests(Caching)
    f_caching.CachingOptimByRequests.fill()
    #parameters(self, network)

    #The class is the f_caching.CachingOptimByCaches(Caching)
    f_caching.CachingOptimByCaches.fill()
    #parameters(self, network)

    #The class is the f_caching.CachingBruteForce(Caching)
    f_caching.CachingBruteForce.fill()
    #parameters(self, network)


def test_utilsPyNotAnActualFunction():
    #module test_utils.py is accessed as test_u

    test_u.test_network_input()
    #parameters (in_dirpath=IN_DIRPATH, sources=SOURCES)

    test_u.test_caching_output()
    #parameters (in_dirpath=OUT_DIRPATH, source='example')

    test_u.test_score()
    #parameters (in_dirpath=IN_DIRPATH, out_dirpath=OUT_DIRPATH,
    # source='example')

    test_u.test_fill()
    #parameters (in_dirpath=IN_DIRPATH, out_dirpath=OUT_DIRPATH,
    # source='example')

    test_u.test_method()
    #parameters (in_dirpath=IN_DIRPATH, out_dirpath=OUT_DIRPATH,
    # sources=SOURCES, caching_method=Caching)

    test_u.main()
    #runs all the tests from test_utils.py
    # test_network_input()
    # test_caching_output()
    # test_score()
    # test_fill()
    #print('\nExecTime: {}'.format(end_time - begin_time))

def utilsPyNotAnActualFunction():
    #module utils.py is accessed as util

    ###Network Class###
    #the class is the util.Network(object)

    util.Network.num_videos()
    # @property parameters (self)
    #returns len(self.videos)

    util.Network.num_endpoints()
    # @property parameters (self)
    #returns len(self.endpoint_latencies)

    util.Network.num_caches()
    # @property parameters (self)
    #returns cache_latencies.shape[1]

    util.Network.num_requests()
    # @property parameters (self)
    #returns len(self.requests)

    util.Network.requests()
    # @property parameters (self)
    #returns self._requests

    util.Network.requests()
    # @requests.setter parameters (self, value)
    #returns self._requests = value

    util.Network.load()
    # @classmethod parameters (cls, filepath)
    #Loads the data from the input file.

    util.Network.save()
    # parameters (filepath, 'w+')
    #Saves the data to the output file.
    #num_videos = self.num_videos
    #num_endpoints = self.num_endpoints
    #num_requests = self.num_requests
    #num_caches = self.num_caches
    #cache_size = self.cache_size

    util.Network.score()
    # parameters (self, caching)
    #returns _score(caching.caches, self.requests,
    # self.cache_latencies, self.endpoint_latencies)

    #__init__(self,videos,endpoint_latencies,
    # cache_size, cache_latencies, requests=None):
    #self.videos = videos
    #self.endpoint_latencies = endpoint_latencies
    #self.cache_size = cache_size
    #self.cache_latencies = cache_latencies
    #self._requests = requests

    #__str__(self):
    #text = '{}: '.format(self.__class__.__name__)
    #names = ['num_videos', 'num_endpoints', 'num_caches', 'num_requests']
    #for name in names:
    #    text += '{}={}  '.format(name, getattr(self, name))
    #return text

    #__repr__(self):
    #return str(self.__dict__)


    ###Caching Class###
    #the class is the util.Caching(object)

    #__init__(self, caches=None):
    #    """
    #    Caching of videos.

    #    Args:
    #        caches (list[set]): The videos contained in each caching server.
    #            The information on the cache size (maximum memory available)
    #            and videos' size is not stored here.
    #    """
    #    try:
    #        iter(caches)
    #    except TypeError:
    #        if caches > 0:
    #            caches = [set() for i in range(caches)]
    #        else:
    #            raise AttributeError(
    #                'Either `caches` or `num_caches` must be supplied!')
    #    finally:
    #        self._caches = caches

    util.Caching.num_caches()
    # @property parameters (self)
    # returns len(self.caches)

    util.Caching.caches()
    # @property parameters (self)
    # returns self._caches

    util.Caching.caches()
    # @caches.setter parameters (self, value)
    # returns self._caches = value

    #__str__(self):
    #    text = '{}: '.format(self.__class__.__name__)
    #    names = ['num_caches']
    #    for name in names:
    #        text += '{}={}  '.format(name, getattr(self, name))
    #    return text


    # __repr__(self):
    #    return str(self.__dict__)

    util.Caching.load()
    # @classmethod parameters (cls, filepath)
    # loads the caches(?) from the input file

    util.Caching.save()
    # @classmethod parameters (self, filepath)
    # saves to the outputfile

    util.Caching.validate()
    # parameters (self, videos, cache_size)
    # returns is_valid = is_valid and (filled <= cache_size)

    util.Caching.score()
    # parameters (self, network)
    # returns _score(self.caches, network.requests,
    # network.cache_latencies, network.endpoint_latencies)

    util.Caching.fill()
    # parameters (self, network)
    # raises an error message if called.


    # @jit
    #_score(caches, requests, cache_latencies, endpoint_latencies):
    #score = 0
    #num_tot = 0
    #for video, endpoint, num in requests:
    #    num_tot += num
    #    latency = max_latency = endpoint_latencies[endpoint]
    #    for cache, videos in enumerate(caches):
    #        if video in videos:
    #            cache_latency = cache_latencies[endpoint, cache]
    #            if cache_latency and cache_latency < latency:
    #                latency = cache_latencies[endpoint, cache]
    #    score += (max_latency - latency) * num
    #score = int(score / num_tot * 1000)
    #return score


####################
#MODULE CALLERS(END)
####################




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

def printToConsole():
    print("howManyVideos variable is " + str(howManyVideos))
    print("howManyEndPoints variable is " + str(howManyEndPoints))
    print("howManyCaches variable is " + str(howManyCaches))
    print("howManyVideos variable is " + str(howManyVideos))
    print("howManyMBsPerCache variable is " + str(howManyMBsPerCache))
    print("videoArray list has " + str(videoArray))
    print("endPointArray list has " + str(endPointArray))
    print("requestArray list has " + str(requestArray))


def saver():
    fileForOutput.write("Hello! this line is saved to the file " + str(fileForOutput))



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
    
#this is the function that uses the countForT to check up that the iterations are not more than what the T variable defines    
def iterationsCheck(hereGoesTheCountForTParameter):
    if hereGoesTheCountForTParameter >= int(T):
        return True
    
#My first thought was to use "for in" loop but after using it I figured out that the use of Range is the best solution.
#As I know, a loop with range is more efficient than the typical "for in" loop.
#Use this function in case of sorting, or in the case of temparated array. you will not regret it.    
def printFromArray(Arrayname, probablytheTVariable):
    for i in range(int(probablytheTVariable)):
        print(str(Arrayname[i]))

def printFromArray2(Arrayname):
    for i in Arrayname:
        print(str(Arrayname[i]))


        
#fills a two-dimensional array with the value N, (the line from the input).
#it needs to get called for every line from the main iteration, (for every N) 
#it needs to work before the twoDimentionalArrayHandler()
#it works optimaly inside the mainCalculativFunction()       
def spliterFunction(strValueFromN):
    global spliterFunctionsArray
    spliterFunctionsArray.append(strValueFromN.split(' ')) 
    
#this is the best way to handle the second dimention of two dimentional array
#it needs to work after the spliterFunction()
#it works optimaly inside the mainCalculativFunction()
#initialy works as sum function
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


def secondLineSpliter(inputFromN):
    videoArrayX.append(inputFromN.split())

def videoArrayRepairer():
    for i in videoArrayX[0]:
        videoArray.append(i)


def endPointHandler(inputFromN, inputForI):
    global countForDwnldN, latency, endPointArray, i
    i = inputForI
    #endPointArray = []*int(howManyEndPoints)
    print("endpointHandler started")
    print("i now is " + str(i))
    endpointvalues = ""
    endpointvalues = inputFromN.split()
    if int(countForDwnldN) == 0:
        print("countForDwnldN is 0")
        print("endpointvalues is " + str(endpointvalues))
        latency = endpointvalues[0]
        print ("latency is " + str(latency))
        countForDwnldN = endpointvalues[1]
        print("countForDwnldN is " + str(countForDwnldN))
        i = int(i) + 1
        endPointArray.append([])
        endPointArray[i - 1].append(latency)
    else:
        print("countForDwnldN is NOT 0")
        print("countForDwnldN is " + str(countForDwnldN))
        print("i is " + str(i))
        endPointArray[i-1].append(endpointvalues)
        countForDwnldN = int(countForDwnldN) - 1
        print("endPointArray is " + str(endPointArray[i-1]))
        #i = int(i) + 1


def endPointReapairer(howManyEndPointsParameter):
    if len(endPointArray) > int(howManyEndPointsParameter):
        endPointArray.pop()

def requestArrayCollector(inputFromN):
    requestArray.append(inputFromN.split(' '))

def requestArrayReapairer(howManyRequestsParameter):
    if len(requestArray) > int(howManyRequestsParameter):
        requestArray.pop()


def insideCaseCalculation(dwnldNparam, dwnldKparam):
    print(int(dwnldNparam) + int(dwnldKparam))

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

class Object2:
    def __init__(self):
        print("I am an object and i just been constructed")
        
class Cote(Object2):
    def __init__(self):
        print("I am an cote and i just been constructed")
        
class Chicken(Cote):
    def __init__(self):
        print("Winner! Winner! Chicken dinner!")
        
class Egg(Cote):
    def __init__(self):
        print("Hello sir! I am an egg and the answer for everything is 42")


#######################
#MAIN() FUNCTION(START)
#######################
    
#The main iteration, (AKA the main loop), now is the main() function. 
#The separation of code to functions blocks keeps the template simple and clear.    
def main():
    countForT
    loader()
    printToConsole()


                
if __name__ == "__main__": main()

#####################
#MAIN() FUNCTION(END)
#####################



#Optimal print example
#print("Case #", str(unregisteredcase), ": ", number_string2, " ",sep="", end='\n', file=f)


fileForInput.close()
fileForOutput.close()
print("That's all folks!")