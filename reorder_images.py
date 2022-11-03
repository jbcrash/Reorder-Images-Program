'''
Author: Josh Bellingham
Version: 2022-10-31
Description: Writing a porgram to reorder a list of images that are numbered in order to easily
place them in a Canva file for printing double sided.
I will start by making a program that can transforms the numbers based on the reuired formula where 
multiples of 4 renamed to be "order(n-3)"
and every other number is renamed to be "order(n+1)"
'''

import os
import time
from PIL import Image as im


#Split file name and file extension

#Defining variables
Dictfn = {}

for f in os.listdir('.'):
    if f.endswith('.jpg'):
        i = im.open(f)
        fn, fext = os.path.splitext(f)
        Dictfn.update({int(fn): f})
    else:
        pass

time.sleep(10) #the program needs a second to process the last file before moving on 

#Math to get the correct order values for the image then rename
for fn, f in Dictfn.items():
    if (fn & 3) == 0:
        n = fn - 3
    else:
        n = fn + 1
    os.rename("C:\\Reorder Images Program\\" + f,
              "C:\\Reorder Images Program\\Reordered Images\\" + str(n) + 'RO' + str(fn) + '.jpg')
        