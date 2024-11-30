import zipfile
import os

def zip_arh(list_file : list[str]):
    homeDir = os.path.expanduser('~')
    
    for i in range(len(list_file) - 1):
        
        with zipfile.ZipFile("arh.zip", mode='a') as ah:
            ah.write(list_file[i][0])