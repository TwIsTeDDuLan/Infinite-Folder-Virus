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
    PATH = ''
    for drive in drives:
        PATH += drive
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
    folders = [folder for folder in os.listdir(PATH)]
    return folders

def file_cruser(PATH):
    folders = list_file(PATH)

    if len(folders) > 0:
        newPATH = PATH
        for folder in folders:
            newPATH += '/' + folder
            file_cruser(newPATH)
        
