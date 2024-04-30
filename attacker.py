import os

#get the current path
#get the current folder names
#create 5 folder copys
    #0,1,2,3,5
#change the original folder's name
    #0th one into 3rd folder
drives = []
#folders = []



def main():
    drive_getter()

    for drive in drives:
        Path = ""
        Path += drive
        #Path = "C:/mber"
        drive_is_done = False
        folder_is_done = False
        folder_explore(folder_is_done,Path)

def drive_getter():
    #drive checker
    for drive in range(ord('A'), ord('Z') + 1):
        drive = chr(drive) + ':/'
        if os.path.exists(drive):
            drives.append(drive)

def folder_getter(path):
    folders = [folder for folder in os.listdir(path) if os.path.isdir(os.path.join(path, folder)) and folder[0] != '$']
    return folders

def duplicate(folder):
    count = 1
    original_name = folder
    print(original_name)
    new_name = f"{folder}{count}"

     #for the begining 5 copies of folders
    while count != 6:
        new_name = f"{folder}{count}"
        try:
            os.mkdir(new_name)
            count += 1
        except:
            pass
            count += 1

def folder_explore(folder_is_done,Path):
    #get into a file
    #create duplicates
    #if files inside
        #repeat
    if folder_is_done == False:
         if os.path.isdir(Path):
            folders = folder_getter(Path)
            if folders:
                os.chdir(Path)
                for folder in folders:
                    duplicate(folder)
                
                old_path = Path
                for folder in folders:
                    Path = old_path
                    Path += f"/{folder}"
                    folder_explore(folder_is_done,Path)
            else:
                 folder_is_done = True
    return

def folder_explore2(folder_is_done,Path):
    while folder_is_done == False:
            if os.path.isdir(Path):
                folders = folder_getter(Path)
                old_path = Path
                if len(folders) != 0:
                    os.chdir(Path)
                    for folder in folders:
                                duplicate(folder)
                                Path += f"/{folder}"
                                print(Path)
                                #folder_explore(folder_is_done,Path)
                else:
                    folder_is_done = True
            else:
                 folder_is_done = True

if __name__ == "__main__":
    main()