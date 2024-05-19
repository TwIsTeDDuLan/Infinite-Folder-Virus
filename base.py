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
    PATH = 'E:/Abb'
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
    try:
        folders = [folder for folder in os.listdir(PATH) if os.path.isdir(os.path.join(PATH, folder)) and folder[0] != '$']
        return folders
    except:
        return ''

def file_cruser(PATH):
    folders = list_file(PATH)

    if len(folders) > 0:
        for folder in folders:
            newPATH = PATH
            newPATH += '/' + folder
            print("Currently in:\n",newPATH)
            file_cruser(newPATH)
            Duplicate(PATH,folder)

    else:
        newPathList = PATH.rsplit('/',1)
        Path = newPathList[0]
        FolderName = newPathList[1]
        Duplicate(Path,FolderName)

def Duplicate(PATH,Name):
    print("Duplicated:\n",PATH,f"({Name})")
    duplicatedFolders = []
    os.chdir(PATH)
    
    duplicates = 5
    for i in range(duplicates):
        newName = f"{Name}{i}"
        try:
            os.mkdir(newName)
            duplicatedFolders.append(newName)
        except:
            pass

    max = len(duplicatedFolders) - 1
    index = random.randint(0,max)
    src = PATH + '/' + Name
    dest = PATH + '/' + duplicatedFolders[index]
    destination = shutil.move(src,dest)

main()