import os
import shutil
import random

#get into a drive
#Duplicate the folders
    #change the original file
    #if there are files inside of it
        #redo duplicate
    #else
        #redo getinto
#redo 

def main():
    drives = list_drives()
    PATH = 'E:/'
    #for drive in drives:
    #PATH += drive
    file_cruser(PATH)
    return

def list_drives():
    drives = []

    for drive in range(ord('A'),ord('Z') + 1):
        drive_letter = chr(drive) + ':/'
        if os.path.exists(drive_letter):
            drives.append(drive_letter)
    
    return drives

def list_file(PATH):
    folders = [folder for folder in os.listdir(PATH) if os.path.isdir(os.path.join(PATH, folder)) and folder[0] != '$']
    return folders

def file_cruser(PATH):
    folders = list_file(PATH)
    newPATH = PATH

    if len(folders) > 0:
        for folder in folders:
            newPATH += '/' + folder
            file_cruser(newPATH)
        print(newPATH)

    else:
        delimiter = "/"
        PathForDuplication = newPATH
        delimiter_count = PathForDuplication.count(delimiter)

        for i in range(delimiter_count):
            print(PathForDuplication)
            ListForDuplication = PathForDuplication.rsplit("/", 1)
            NewPathForDuplication = ListForDuplication[0]
            Duplicate(NewPathForDuplication)
            PathForDuplication = NewPathForDuplication



def Duplicate(PATH):
    return

main()
