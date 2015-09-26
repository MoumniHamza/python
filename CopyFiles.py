import shutil

source = ("a/file 2.txt" , "a/file 3.txt" , "a/file 4.txt" )
destination ="b/"

for files in source:
    shutil.copy(files , destination)
    print(files)
