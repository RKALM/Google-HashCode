itIsTheFirstLine = True     #This variable is about the input line. If the line is the first the variable itIsTheFirstLine is True.
T=0     #The number of lines with usefull Data. the number of tierations.
result = "Not any result right now" #this is used for the result wich is printed in the end of the code with the default value.
testSum = 0 #This is used to make the mainCheckFunction() bit more interesting but making the function to work as add function.
countForT = 0 #this is the count vairiable that helps to check that the iterations are not more than the predefined T variable.
countForDwnldN = 0
dwnldK = 0
caserArray = []
i = 0
fileForOutput = open('output.txt','w')
fileForInput = open('input.in','r')


#the mainCheckFunction() function is doing the necessary checking before the mainCalculativFunction().
#there is always something to check
def mainCheckFunction(checkFunctionsProperty):
        if checkFunctionsProperty == True:
                return True

def loader():
    global result, countForT
    for N in fileForInput:
        print("itIsTheFirstLine now is " + str(itIsTheFirstLine))
        fileForOutput.write("itIsTheFirstLine now is " + str(itIsTheFirstLine))
        # print("itIsTheFirstLine now is " + str(itIsTheFirstLine) end='\n' file=f)
        if itIsTheFirstLine == True:
            firstLineCorrection(N)
        else:
            caser(N, i)
            #countForT = countForT + 1
    #print(str(caserArray))



def save():
        print(str(caserArray))
        fileForOutput.write(str(caserArray))

# this the function that break the stream to cases
# this function is inspired by the DWNLD problem on codechef
# please use global i and countForDwnldN outside the function
#on the parameter of inputForI just insert the global variable I
# also use the repair function to repair the caserArray
def caser(inputFromN, inputForI):
    global countForDwnldN, dwnldK, caserArray, i
    i = inputForI
    print("caser started")
    print("i now is " + str(i))
    caserTemporalValues = ""
    caserTemporalValues = inputFromN.split()
    if int(countForDwnldN) == 0:
        print("countForDwnldN is 0")
        print("caserTemporalValues is " + str(caserTemporalValues))
        dwnldK = caserTemporalValues
        print("dwnldK is " + str(dwnldK))
        countForDwnldN = caserTemporalValues[1]
        print("countForDwnldN is " + str(countForDwnldN))
        #super sos. I am still trying to figure out i.
        #statment below, active by default.
        #the problem is probably a +1, -1 bug.
        i = int(i) + 1
        caserArray.append([])
        caserArray[i - 1].append(dwnldK)
        #print(str(caserArray))
    else:
        print("countForDwnldN is NOT 0")
        print("countForDwnldN is " + str(countForDwnldN))
        #i = int(i) + 1
        print("i is " + str(i))
        caserArray[i - 1].append(caserTemporalValues)
        countForDwnldN = int(countForDwnldN) - 1
        print("caserArray is " + str(caserArray[i - 1]))
        #i = int(i) + 1
        #print(str(caserArray))

# it needs to run after the caser()
# it repairs if necessary, (and if possible), the caserArray
# it repairs caserArray by removing the empty trailer.
def caseReapairer(howManyCasesParameter):
    if len(caserArray) > int(howManyCasesParameter):
        caserArray.pop()

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
    
#The main iteration, (AKA the main loop), now is the main() function. 
#The separation of code to functions blocks keeps the template simple and clear.    
def main():
    global countForT
    loader()
    save()
                
if __name__ == "__main__": main()



#Optimal print example
#print("Case #", str(unregisteredcase), ": ", number_string2, " ",sep="", end='\n', file=f)


fileForInput.close()
fileForOutput.close()
print("That's all folks!")

