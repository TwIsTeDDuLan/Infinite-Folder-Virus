

import os

def FolderRemove():
    os.chdir("E:/Abb")
    folders = [folder for folder in os.listdir("E:/Abb")]
    for folder in folders:
        os.remove(f"E:/Abb/{folder}")
    return

def folderMaker():
    os.chdir("E:/Abb")
    for i in range(4):
        os.mkdir(chr(97+i))
    
    os.chdir("E:/Abb/a")

    for i in range(3):
        os.mkdir(chr(97+i))


def main():
    inp = int(input("what want?"))
    if inp == 1:
        folderMaker()
    else:
        FolderRemove()

try:
    while True:
        main()
except:
    while True:
        main()