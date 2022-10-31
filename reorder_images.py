'''
Author: Josh Bellingham
Version: 2022-10-31
Description: Writing a porgram to reorder a list of images that are numbered in order to easily
place them in a Canva file for printing double sided.
I will start by making a program that can transforms the numbers based on the reuired formula where 
multiples of 4 renamed to be "order(n-3)"
and every other number is renamed to be "order(n+1)"
'''


for i in range(0, 24):
    i = i + 1
    if (i & 3) == 0:
        print("Yes,", i, "is a multiple of 4")
    else:
        print("No,", i,"is not a multiple of 4")
        