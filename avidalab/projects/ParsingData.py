import re
import os
#Function for parsing the file for the column names
#Passing file name as argument
def parseFile(file):
    file = os.path.abspath(file)
    #Opening file
    with open(file, 'r') as f:
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
        f.close()
        #Returns array of column names
        return colNames