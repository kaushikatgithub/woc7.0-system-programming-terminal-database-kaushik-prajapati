import os
## Simple Commands

# Get present working directory
print(os.getcwd())

# Change working directory
os.chdir("C:\\Users\\Kaushik\\Desktop")
print(os.getcwd())

# List Directories and Files, inside a particulary Directory
files = os.listdir(os.getcwd())
print(type(files))
print(files)

# Create New Directory
os.mkdir("Python")

# Recursive Directories are allowed
os.makedirs("Languages/C++/Module-1", exist_ok=True)

# Remove Directory
os.rmdir("Python")

# Walk through the directories
for dirpath, dirnames, filenames in os.walk("C:\\Users\\Kaushik\\Desktop\\Languages"):
    print("Current Directory Path: ", dirpath)
    print("Directories in pwd: ", dirnames)
    print("Files in pwd: ", filenames)
    print("")