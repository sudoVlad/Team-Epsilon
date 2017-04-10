import re

#Function for parsing the file
def parseFile(f):
    #Array for name of Columns
    colNames = []

    for line in f:
        #Regex matching to find column 1 - X
        match = re.search(r'^#\s*[0-9]*:', line)
        if match:
            #Stripping the line and adding it to the array
            index = line.index(':')
            columnName = line[index + 1:]
            #Strip the newline carriage
            columnName = columnName.strip('\n')
            #Strip the whitespace from the beginning and end of string
            columnName = columnName.strip()
            #Adding columns to the array
            colNames.append(columnName)
    f.close();
    #Print to see if it works
    return colNames

#Hard coded to open and read the dominant.dat file
f = open('dominant.dat', 'r')
parseFile(f)
