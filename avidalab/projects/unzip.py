import os, zipfile
from . models import Project
dir_name = os.curdir
extension = ".zip"

os.chdir(dir_name) # change directory from working dir to dir with files

for item in os.listdir(dir_name): # loop through items in dir
    if item.endswith(extension): # check for ".zip" extension
        file_name = os.path.abspath(item) # get full path of files
        zip_ref = zipfile.ZipFile(file_name) # create zipfile object
        zip_ref.extractall(dir_name) # extract file to dir
        zip_ref.close() # close file
        #os.remove(file_name) # delete zipped file

   # if item.endswith(".gz"):
    #    file_name=os.path.abspath(item)

