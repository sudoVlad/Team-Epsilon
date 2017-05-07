import re

#Function for parsing the file for the column names
#Passing file name as argument
def parseFile(file):
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
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 29588afc6ef1d1ac07a329dd1a9dd6294af6f78d
        return colNames

#Function for parsing the file for the actual data that will be returned as a dictionary
#Passing file name as argument
def mapData(file):
    #Array of column names
    columns = parseFile(file)

    #Initial dictionary of column names(keys) set to empty lists(values)
    dictOfData = {key: [] for key in columns}

    #Initialize array with all the keys
    keys = []
    for key in dictOfData:
        keys.append(key)

    #Opening file
    with open(file, 'r') as f:
        for line in f:
            #Regex matching to find column 1 - X
            match = re.search(r'^#\s*[0-9]*:', line)
            #Using the regex to
            #Skip the comments to parse the data columns
            if not match:
                #Taking a line of data and breaking it into a list
                #where each index of the list refers to each data column
                data = line.split(" ")
                #initialized i to 0 to access the keys
                i = 0
                #Parse through the list of data and put data at each index into
                #the dictionary for each key
                for column in data:
                    #Strip the newline carriage because the last column will have one
                    column = column.strip('\n')
                    dictOfData[keys[i]].append(column)
                    i += 1
        f.close()
        #Return dictionary of the keys(name of each column) mapped to its values(list of data for each column)
        return dictOfData
<<<<<<< HEAD
=======
        return colNames
>>>>>>> master
=======
>>>>>>> 29588afc6ef1d1ac07a329dd1a9dd6294af6f78d
