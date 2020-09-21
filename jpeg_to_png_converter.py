import sys
import os
from PIL import Image, ImageFilter, EpsImagePlugin
#grab first and second argument
try: 
   in_folder = sys.argv[1]
   out_folder = sys.argv[2]
   os.makedirs(out_folder, exist_ok=True)
#loop through input folder
   for filename in os.listdir(in_folder):
      if filename.endswith('.jpg'):
         img = Image.open(os.path.join(in_folder, filename))
         filebase = os.path.splitext(filename)[0]
#convert all images to PNG and save to new folder
         img.save (os.path.join(out_folder, filebase) + '.png', 'PNG')
         print (f'Converting {in_folder} {filename} ---> {out_folder} {filebase}.png image.')
         continue
      else:
         continue

except IndexError as err:
        print(f'Please enter folder name! Error reason: {err} ')
