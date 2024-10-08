import os,shutil,random,ctypes,sys
from EnvCreator import folderMaker

FILE = open("E:/logCTF.txt","w")

TotalDuplications = [0]
TotalMoves = [0]
TotlInaccecibleFiles = [0]
TotalUnsuccessfulTreeDuplications = [0]
TotalUnsuccessfulFolderDuplications = [0]

def main():
    #"E:/Abb/"
    PATH = 'E:/'
    drives = list_drives()
    #for drive in drives:
        #PATH += drive
    drive = "E:/"
    folderMaker(drive)
    PATH += "Abb/"
    file_cruser(PATH)
    

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
            NextFolders = list_file(newPATH)
            if len(NextFolders) > 0:
                try:
                    Duplicate(PATH,folder)
                except Exception as e:
                    print(f"Couldn't duplicate the tree:{e}")
                    TotalUnsuccessfulTreeDuplications[0] += 1
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
            TotalUnsuccessfulFolderDuplications[0] += 1

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
            TotalDuplications[0] += 1
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
        TotalMoves[0] += 1
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
            txt = f"DUPLICATIONS: {TotalDuplications[0]} \n Moves: {TotalMoves} \n TreeFails: {TotalUnsuccessfulFolderDuplications} \n FolderFails: {TotalUnsuccessfulFolderDuplications}"
            FILE.write(txt)
            FILE.close()
            shutil.rmtree("E:/Abb")
            try:
                os.chdir("E:/")
                os.system("logCTF.txt")
            except:
                input("couln't open long file")
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
        except Exception as e:
            print(f"Failed to elvavate to admin previlages: {e}")
            input("Press Enter to exit...")


