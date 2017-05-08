import os, zipfile, gzip

dir_name = os.curdir
extension = ".zip"
extension2 = ".tar.gz"

os.chdir(dir_name) # change directory from working dir to dir with files

for item in os.listdir(dir_name): # loop through items in dir
    if item.endswith(extension): # check for ".zip" extension
        file_name = os.path.abspath(item) # get full path of files
        zip_ref = zipfile.ZipFile(file_name) # create zipfile object
        zip_ref.extractall(dir_name) # extract file to dir
        zip_ref.close() # close file
        #os.remove(file_name) # delete zipped file

    if item.endswith(extension2): # check for .gz 
        file_name2 = os.path.abspath(item) # get path for file
        inF = gzip.GzipFile(file_name2, 'rb')
        s = inF.read()
        inF.close()

        outF = file(file_name2, 'wb')
        outF.write(s)
        outF.close()


def unzip_project(id):
    return