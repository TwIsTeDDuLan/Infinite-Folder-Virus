import shutil
import os

src = "D:\TV-Series/3 Body Problem1"
dest = "D:\TV-Series/3 Body Problem2/"
files = os.listdir(src)
if files:
    print("there are files")
    pass
else:
    print("didnt work")
shutil.move(src,dest)