import os

## File System Path Methods

# Add files or folders to the path 
pwd = os.getcwd()
folder = "Files"
file = "sample.txt"

joined_path = os.path.join(pwd, folder, file)
print(joined_path)

# Check for the existence of the path
print(os.path.exists(joined_path))

# Check weather the path is a directory or a file
print(os.path.isdir(joined_path))
print(os.path.isfile(joined_path))

# Filename and Directory names from a path
print(os.path.basename(joined_path))
print(os.path.dirname(joined_path))
print(os.path.split(joined_path))
print(os.path.splittext(joined_path)) # Split extension

# Get the information regarding the file
statistics = os.stat(joined_path)
print(type(statistics))
print(statistics)

# Get environment variables
paths = os.environ.get("PATH")
print(paths)

# Logged in User
print(os.getlogin())
