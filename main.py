
# Modification date: Fri Jan 19 18:21:03 2024

# Production date: Fri Jan 19 16:55:20 2024

import os.path, time

from os import listdir
from os.path import isfile, join

def writeToFile(filePath):
    if filePath[-4:] == ".txt" or filePath[-3:] == ".py":
        print(">>>File ends with txt or py, writing...")
        filer = open(filePath, 'r')
        fileLines = filer.readlines()
        prodate = "# Production date: " + str(time.ctime(os.path.getctime(filePath)) + "\n")
        moddate = "\n# Modification date: " + str(time.ctime(os.path.getmtime(filePath)) + "\n\n")
        fileLines.insert(0, "\n")
        fileLines.insert(0, prodate)
        fileLines.insert(0, moddate)
        filer.close()
        
        filew = open(filePath, 'w')
        filew.writelines(fileLines)
        filew.close()
        print(">>>Written: " + moddate + prodate)


def goToFiles(currentPath):
    print("\n\n\nCurrently in: " + currentPath)
    
    files = []
    dirs = []
    
    for f in listdir(currentPath):
        if isfile(join(currentPath, f)):
            files.append(join(currentPath, f))
        else:
            dirs.append(join(currentPath, f))
    
    
    for file in files:
        print("\n>Will try to write file: " + file)
        writeToFile(file)
    
    for direc in dirs:
        print(direc)
        if direc[-8:] != "Astro_Pi":
            goToFiles(direc)
        



def main():
    targetfolder = input("Enter the folder you want to write its files' date of mod and production: ")
    goToFiles(os.getcwd() + targetfolder)
    

main()