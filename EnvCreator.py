import ctypes
import os,sys,shutil

def FolderRemove():
    
    shutil.rmtree(f"E:/Abb/")

def folderMaker():
    os.chdir("E:/")
    os.mkdir("Abb")
    os.chdir("E:/Abb/")

    for i in range(2):
        os.mkdir(chr(97+i))
    
    #os.chdir("E:/Abb/b")

    #for i in range(3):
        #os.mkdir(chr(97+i))

    os.chdir("E:/Abb/a")

    for i in range(3):
        os.mkdir(chr(97+i))

    os.chdir("E:/")
    return

def IsAdmin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    
def main():
    while True:
        os.system('cls')
        inp = int(input("1.Create\n2.Remove\n"))
        if inp == 1:
            folderMaker()
        
        elif inp == 2:
            FolderRemove()

        else:
            pass

if __name__ == "__main__":
    if IsAdmin():
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