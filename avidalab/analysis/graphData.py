#For grabbing the dictionary with data
from . ParsingData import parseFile, mapData

#For graphing purposes
import matplotlib.pyplot as plot
import pylab

#To use the numpy library
import numpy as np

#For regex purposes
import re

#For creating the /static/graphs/ directory to save the images files
import os

#Grab the directory name analysis and then create the the static/graphs/ directory under it
#for the images to be saved in
script_dir = os.path.dirname(__file__)
results_dir = os.path.join(script_dir, 'static/graphs/')
if not os.path.isdir(results_dir):
    os.makedirs(results_dir)

# mean array maker takes an array of arrays and creates an array that contains the mean array as defined below
# [1, 2, 3], [4, 5, 6], [7, 8, 9]
# the result would be [6, 7.5, 9]
#
def mean_array_maker(arrays):
    result = []
    if len(arrays) == 0:
        return result

    min_size = len(arrays[0])

    #grab the min size to make all arrays the same size
    for array in arrays:
        min_size = min(min_size, len(array))
    # make all arrays the same size
    for array in arrays:
        result.append(array[:min_size])

    #do the mean array stuff
    np_arrays = np.array(result)
    mean_array = np_arrays.mean(axis=0)
    return mean_array

#Function for graphing scatter plot using the dictionary
def graphScatter(listOfDictionaries, fieldName):
    #Initiated empty list of arrays, this will contain a list of all the
    #lists that are of the same fieldName
    listOfArrays = []

    #Loop through the list of dictionaries to get a list of the keys, from
    #the keys we will then check for a match
    for dictionary in listOfDictionaries:
        listOfKeys = list(dictionary.keys())

        #Looping through the list of keys(field names aka column names), if it matches
        #we will then cast that list to floats then add the list to our list of arrays(aka list of lists)
        for key in listOfKeys:
            m = re.match(fieldName, key, re.IGNORECASE)
            if bool(m):
                listOfArrays.append(list(map(float, dictionary[key])))

    #The mean list(array) of all the lists of the same fieldName
    averageOfLists = mean_array_maker(listOfArrays).tolist()

    #Time array to graph against time
    timeArray = []
    i = 1;
    for n in averageOfLists:
        timeArray.append(i)
        i += 1

    #Labeling the title, x-axis, y-axis, then plotting
    plot.title('Time vs ' + fieldName)
    plot.xlabel(fieldName)
    plot.ylabel('Time')
    plot.scatter(averageOfLists, timeArray)

    #Displaying the graph
    #plot.show()

    #Saving the plotted graph to /static/graphs/scatter_plot.png
    plot.savefig(results_dir + 'scatter_plot.png')
    plot.clf()

#Function for graphing histogram using the dictionary
def graphHistogram(listOfDictionaries, fieldName):
    #Initiated empty list of arrays, this will contain a list of all the
    #lists that are of the same fieldName
    listOfArrays = []

    #Loop through the list of dictionaries to get a list of the keys, from
    #the keys we will then check for a match
    for dictionary in listOfDictionaries:
        listOfKeys = list(dictionary.keys())

        #Looping through the list of keys(field names aka column names), if it matches
        #we will then cast that list to floats then add the list to our list of arrays(aka list of lists)
        for key in listOfKeys:
            m = re.match(fieldName, key, re.IGNORECASE)
            if bool(m):
                listOfArrays.append(list(map(float, dictionary[key])))

    #The mean list(array) of all the lists of the same fieldName
    averageOfLists = mean_array_maker(listOfArrays).tolist()

    #Labeling the title, x-axis, then plotting
    plot.title('Histogram of ' + fieldName)
    plot.xlabel(fieldName)
    plot.hist(averageOfLists, bins=30)

    #Saving the plotted graph to /static/graphs/histogram.png
    plot.savefig(results_dir + 'histogram.png')
    plot.clf()
    #Displaying the graph
    #plot.show()

#Function for graphing the line graph using the dictionary
def graphLineGraph(listOfDictionaries, fieldName):
    #Initiated empty list of arrays, this will contain a list of all the
    #lists that are of the same fieldName
    listOfArrays = []

    #Loop through the list of dictionaries to get a list of the keys, from
    #the keys we will then check for a match
    for dictionary in listOfDictionaries:
        listOfKeys = list(dictionary.keys())

        #Looping through the list of keys(field names aka column names), if it matches
        #we will then cast that list to floats then add the list to our list of arrays(aka list of lists)
        for key in listOfKeys:
            m = re.match(fieldName, key, re.IGNORECASE)
            if bool(m):
                listOfArrays.append(list(map(float, dictionary[key])))

    #The mean list(array) of all the lists of the same fieldName
    averageOfLists = mean_array_maker(listOfArrays).tolist()

    #Labeling the title, x-axis, then plotting
    plot.title('Line graph of ' + fieldName + ' vs Time')
    plot.xlabel('Time')
    plot.ylabel(fieldName)
    plot.plot(averageOfLists)

    #Saving the plotted graph to /static/graphs/line_graph.png
    plot.savefig(results_dir + 'line_graph.png')
    plot.clf()
    #Displaying the graph
    #plot.show()

#Function for graphing the box and whisker plot using the dictionary
def graphBoxAndWhisker(listOfDictionaries, fieldName):
    #Initiated empty list of arrays, this will contain a list of all the
    #lists that are of the same fieldName
    listOfArrays = []

    #Loop through the list of dictionaries to get a list of the keys, from
    #the keys we will then check for a match
    for dictionary in listOfDictionaries:
        listOfKeys = list(dictionary.keys())

        #Looping through the list of keys(field names aka column names), if it matches
        #we will then cast that list to floats then add the list to our list of arrays(aka list of lists)
        for key in listOfKeys:
            m = re.match(fieldName, key, re.IGNORECASE)
            if bool(m):
                listOfArrays.append(list(map(float, dictionary[key])))

    #The mean list(array) of all the lists of the same fieldName
    averageOfLists = mean_array_maker(listOfArrays).tolist()

    plot.title('Box and Whisker Plot of ' + fieldName)
    plot.ylabel(fieldName)
    plot.boxplot(averageOfLists)

    #Saving the plotted graph to /static/graphs/box_and_whisker_plot.png
    plot.savefig(results_dir + 'box_and_whisker_plot.png')
    plot.clf()
    #Displaying the graph
    #plot.show()

#Function for testing the graph functions
def TestToShow():
    #Testing functions by getting a dictionary(data from a .dat file)
    dictionaryOfData = mapData("dominant.dat")
    dictionaryOfData2 = mapData("count.dat")

    #Appending dictionaries to listOfDicts
    listOfDicts = []
    listOfDicts.append(dictionaryOfData)
    listOfDicts.append(dictionaryOfData2)

    #Testing graphs with list of dictionaries and fieldname(column name)
    #graphScatter(listOfDicts, 'Update')
    #graphHistogram(listOfDicts, 'Update')
    #graphLineGraph(listOfDicts, 'Update')
    #graphBoxAndWhisker(listOfDicts, 'Update')
