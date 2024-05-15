import os
import shutil
import random
#get the current path
#get the current folder names
#create 5 folder copys
    #0,1,2,3,5
#change the original folder's name
    #0th one into 3rd folder
drives = []

def main():
    drive_getter()

    #for drive in drives:
        #Path = ""
        #Path += drive
    Path = "D:\TV-Series"
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

def duplicate(folder,Path):
    count = 1
    original_name = folder
    new_name = f"{folder}{count}"
    folders_count = 6
    duplicate_folders = []

    while count != folders_count:
        new_name = f"{folder}{count}"
        try:
            os.mkdir(new_name)
            duplicate_folders.append(new_name)
            count += 1
        except:
            duplicate_folders.append(new_name)
            count += 1

    #to identify the original folders so that duplicated files wont moved
    src = Path + '/' + original_name
    files = os.listdir(src)
    if files:
        pass
    else:
        return
    

    Done = False
    while Done == False:
        max = len(duplicate_folders)-1
        index = random.randint(0,max)
        if duplicate_folders[index] != original_name:
            dest = Path + '/' + duplicate_folders[index] + '/'
            Done = True

    print(src, dest)
    destination = shutil.move(src, dest)
    
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
                    duplicate(folder,Path)
                
                old_path = Path
                for folder in folders:
                    Path = old_path
                    Path += f"/{folder}"
                    folder_explore(folder_is_done,Path)
            else:
                 folder_is_done = True

if __name__ == "__main__":
    main()