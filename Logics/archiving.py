import zipfile
import os

def zip_arh(list_file : list[str]):
    path = list_file[0]
    
    for i in range(len(path)):
        
        with zipfile.ZipFile("arh.zip", mode='a') as ah:
            ah.write(path[i])