import os

folders = [folder for folder in os.listdir("E:/") if os.path.isdir(os.path.join("E:/", folder))]

print(folders)