'date created'
'authors'

import PIL as pillow
import os

project_dir = r"C:\Users\sharikgorilla176\OneDrive\Pictures\NFTs\NAWT\Generate"

layers_list = [item[1] for item in os.walk(project_dir)][0]

print(layers_list)