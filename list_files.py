import os

# get the path of current folder
path = os.getcwd()

# iterate over all the folders and subfolders and list all the files
for root, dirs, files in os.walk(path):
    
    # ignore the hidden files who's naming starts with dot(.)
    dirs[:] = [d for d in dirs if not d.startswith('.')]

    for dir in dirs:
        print(os.path.join(root, dir))
    for file in files:
        print(os.path.join(root, file))


