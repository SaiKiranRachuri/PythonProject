import sys
import os

from PIL import Image
count=0

img_folder=sys.argv[1]                            #Alternatively we can take input from cmd using statement as input("Enter a source folder with \ : ")
out_folder=sys.argv[2]



if not os.path.exists(out_folder):
	os.mkdir(out_folder)

for file_name in os.listdir(img_folder):
	img=Image.open(f'{img_folder}{file_name}')
	clean_name=os.path.splitext(file_name)[0]       #This line splits the images by imagename and its extension and returns that in a tuple
	#print(clean_name)
	img.save(f'{out_folder}{clean_name}.png','png')
	count+=1
	print(f'Converting image {count} successful')
