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

    for drive in drives:
        file_cruser(drive)
    return

def list_drives():
    drives = []

    for drive in range(ord('A'),ord('Z') + 1):
        drive_letter = chr(drive) + ':/'
        if os.path.exists(drive_letter):
            drives.append(drive_letter)
    
    return drives

def file_cruser(drive):
    PATH += drive
    