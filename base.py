import os
import shutil
import random
import ctypes
import sys

#get into a drive
#Duplicate the folders
    #change the original file
    #if there are files inside of it
        #redo duplicate
    #else
        #redo getinto
#redo 

def main():
    PATH = 'E:/Abb/'
    drives = list_drives()
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
            try:
                Duplicate(PATH,folder)
            except Exception as e:
                print(f"Couldn't duplicate the tree:{e}")

    else:
        newPathList = PATH.rsplit('/',1)
        Path = newPathList[0]
        FolderName = newPathList[1]
        try:
            Duplicate(Path,FolderName)
        except Exception as e:
            print(f"Couldn't duplicate the folder:{e}")

def Duplicate(PATH,Name):
    print("Duplicated:",PATH,f"({Name})")
    os.chdir(PATH)
    
    duplicates = 5
    for i in range(duplicates):
        newName = f"{Name}{i}"
        try:
            os.mkdir(newName)
        except:
            pass

    duplicatedFolders = [folder for folder in os.listdir(PATH) if Name in folder]
    print(duplicatedFolders)
    
    max = len(duplicatedFolders) - 1
    if max > 1:
        index = random.randint(1,max)
        src = PATH + '/' + Name
        dest = PATH + '/' + duplicatedFolders[index] + '/'
        destination = shutil.move(src,dest)
        print(f"Moved to:{duplicatedFolders[index]}")
    else:
        pass

def duplicate(PATH,folder):
    print("Duplicated:\n",PATH,f"({folder})")

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def Main():
    if is_admin():
        try:
            main()
            input("Press Enter to exit...")
        except Exception as e:
            print(f"An error occurred: {e}")
            input("Press Enter to exit...")
    
    else:
        print("Not running as administrator. Re-running with admin privileges...")
        script = os.path.abspath(sys.argv[0])
        params = ' '.join([script] + sys.argv[1:])
        try:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
            input("Press Enter to exit...")
        except Exception as e:
            print(f"Failed to elvavate to admin previlages: {e}")
            input("Press Enter to exit...")

try:
            main()
            input("Press Enter to exit...")
except Exception as e:
            print(f"An error occurred: {e}")
            input("Press Enter to exit...")