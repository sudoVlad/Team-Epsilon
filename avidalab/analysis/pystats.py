import math
#from scipy.stats import mannwhitneyu
#from scipy.stats.mstats import kruskalwallis

def checkForNonsense(given):
    #check if the list is empty or contains only null values
    if (given == []):
        raise TypeError("Cant do math without numbers. The list we were given is empty.")
    #check if there are non numbers in the list
    if any(not isinstance(item, (int, float, complex)) for item in given):
        raise TypeError("There are non-numbers in the given list.")

#takes in a list of any number type; int,float, etc
#returns mean as float
def mean(given):
    checkForNonsense(given)
    returnValue = 0.0
    for number in given:
         returnValue += number
    return returnValue / len(given)

#returns median as float
def median(given):
    checkForNonsense(given)
    returnValue = 0.0
    #list has to be sorted to find median
    given = sort(given)
    if (len(given) % 2.0 != 0.0):
        return given[int(math.floor(len(given)/2.0))]
    else:
        return mean([(given[int(len(given)/2.0)]), given[int(len(given)/2.0 - 1.0)]])

#returns standard dev as float
def standardDeviation(given):
    checkForNonsense(given)
    #get mean of given list
    u = mean(given)
    squareDiffernces = []
    for number in given:
        #subtact the mean from each number in the list
        #and square it
        temp = (number - u) ** 2
        squareDiffernces.append(temp)
    #take the square root of the mean of those numbers
    return math.sqrt(mean(squareDiffernces))

#from the scipy package
#returns as float a tuple (u,p-value)
#def mannWhitneyU(sample1,sample2):
    #checkForNonsense(sample1)
    #checkForNonsense(sample2)
    #u,p = mannwhitneyu(sample1,sample2)
    #return u,p

#from the scipy package
#takes in any number of lists
#paramater must have at least 2 lists
#each list must have at least 5 samples
#because of the way this test works
#returns tuple (H,p-value) both are float
#def kruskalWallisH(*listOfSamples):
    #for arg in listOfSamples:
        #if(len(arg) < 5):
            #raise ValueError("there must be at least 5 samples in each list")
        #checkForNonsense(arg)
    #for arg in listOfSamples:
        #sort(arg)
    #if(len(listOfSamples) >= 2):
        #h,p = kruskalwallis(listOfSamples)
        #return h,p
    #else:
        #raise ValueError("There must be at least two sample lists")

#standard quicksort
def sort(given):
    less = []
    equal = []
    greater = []
    if len(given) > 1:
        pivot = given[0]
        for x in given:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return sort(less)+equal+sort(greater)
    else:
        return given