import ctypes
import os,sys,shutil

def FolderRemove(drive):
    shutil.rmtree(f"{drive}Abb/")

def folderMaker(drive):
    os.chdir("E:/")
    os.mkdir("Abb")
    os.chdir(f"{drive}Abb/")

    for i in range(2):
        os.mkdir(chr(97+i))
    
    os.chdir(f"{drive}Abb/b")

    for i in range(3):
        os.mkdir(chr(97+i))

    os.chdir(f"{drive}Abb/a")

    for i in range(3):
        os.mkdir(chr(97+i))

    os.chdir(drive)
    
def EnvCreator(inp,drive, FILE):
    if inp == 1:
        try:
            folderMaker(drive)
            return 1
        except Exception as e:
            FILE.write(f"\n{e}\n")
            input(f"File creation error.:{e}")
            return 2

    elif inp == 2:
        try:
            FolderRemove(drive)
            return 1
        except Exception as e:
            FILE.write(f"\n{e}\n")
            input(f"File deletion error.:{e}")
            return 2
    else:
        return 3
        pass