#For grabbing the dictionary with data
from ParsingData import parseFile, mapData

#For graphing purposes
import matplotlib.pyplot as plot
import pylab

#Function for graphing scatter plot using the dictionary
def graphScatter(dictionary):
    #Getting the column(list) called Average Gestation Time of the Dominant Genotype's data
    x = dictionary['Average Gestation Time of the Dominant Genotype']

    #Hardcoded because list has a string that can't be converted to float, so needs to be deleted
    del x[:2]

    #x is a list of data(Average Gestation Time of the Dominant Genotype), this typecasts the list which were strings to floats
    #to be plotted
    x = list(map(float, x))

    #Getting the column(list) called Update
    y = dictionary['Update']

    #Hardcoded because list has a string that can't be converted to float, so needs to be deleted
    del y[:3]

    #y is a list of data(Update), this typecasts the list which were strings to floats
    #to be plotted
    y = list(map(float, y))

    #Labeling the title, x-axis, and y-axis, then plotting
    plot.title('Update vs Average Gestation Time of the Dominant Genotype')
    plot.xlabel('Average Gestation Time of the Dominant Genotype')
    plot.ylabel('Update')
    plot.scatter(x, y)

    #Saving the plotted graph as 'testScatter.png'
    #plot.savefig('testScatter.png')

    #Displaying the graph
    plot.show()

#Function for graphing histogram using the dictionary
def graphHistogram(dictionary):
    #Getting the column(list) called Average Merit of the Dominant Genotype
    y = dictionary['Average Merit of the Dominant Genotype']

    #Hardcoded because list has a string that can't be converted to float, so needs to be deleted
    del y[:2]

    #y is a list of data(Average Merit of the Dominant Genotype), this typecasts the list which were strings to floats
    #to be plotted
    y = list(map(float, y))

    #Labeling the title, y-axis, then plotting
    plot.title('Histogram')
    plot.ylabel('Average Merit of the Dominant Genotype')
    plot.hist(y, bins=30)

    #Saving the plotted graph as 'testHistogram.png'
    #plot.savefig('testHistogram.png')

    #Displaying the graph
    plot.show()

#Function for graphing the line graph using the dictionary
def graphLineGraph(dictionary):
    #Getting the column(list) called Number of Birth's data
    y = dictionary['Number of Births']

    #y is a list of data(Number of Birth's), this typecasts the list which were strings to floats
    #to be plotted
    y = list(map(float, y))

    #Labeling the title, y-axis, x-axis, then plotting
    plot.title('Number of Births vs Time')
    plot.ylabel('Number of Births')
    plot.xlabel('Time')
    plot.plot(y)

    #Saving the plotted graph as 'testLineGraph.png'
    #plot.savefig('testLineGraph.png')

    #Displaying the graph
    plot.show()

#Function for graphing the box and whisker plot using the dictionary
def graphBoxAndWhisker(dictionary):
    #Getting the column(list) called Number of Birth's data
    y = dictionary['Abundance of Dominant Genotype']

    #y is a list of data(Number of Birth's), this typecasts the list which were strings to floats
    #to be plotted
    y = list(map(float, y))

    plot.title('Box and Whisker Plot')
    plot.ylabel('Abundance of Dominant Genotype')
    plot.boxplot(y)

    #Saving the plotted graph as 'testBoxAndWhisker.png'
    #plot.savefig('testBoxAndWhisker.png')

    #Displaying the graph
    plot.show()

def TestToShow():

    #This is the dictionary of data we get from calling the mapData function from
    #our ParsingData.py file
    dictionaryOfData = mapData("dominant.dat")

    #Calling the functions to display the various graphs
    graphScatter(dictionaryOfData)
    graphHistogram(dictionaryOfData)
    graphLineGraph(dictionaryOfData)
    graphBoxAndWhisker(dictionaryOfData)
