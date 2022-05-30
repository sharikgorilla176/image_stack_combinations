'date created'
'authors'

import PIL.Image as pillow
import os

project_dir = r"C:\Users\sharikgorilla176\OneDrive\Pictures\NFTs\NAWT\Generate"

#create list of directory for all files with layer numbering
layers_list = []
for root, dirs, files in os.walk(project_dir):
    if len(files) != 0:
        for file in files:
            if file[0].isdigit() == False:
                print(file, 'please label your filename as instructed in README.md')
            else:
                layers_list.append(root + "\\" + file)
            
            
        
for layers in layers_list:
    print(layers.split("\\")[-1])