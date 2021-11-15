""" 
IMPORTANT! 
The image must be the proper size before running the program
This program simply makes and excel file the same size as the image. 

To see how to set up and run this program, read the README.txt file
"""

import pygame
import pandas as pd
import sys

# Get the image and its dimensions
src_img = pygame.image.load(sys.argv[1])
w = src_img.get_width()
h = src_img.get_height()
arr = []

# For each pixel in the image, put its RGB values into a tuple and append that tuple to a 2D array
for row in range(h):
    col_arr = []
    for col in range(w):
        (r, g, b, a) = src_img.get_at((col, row))
        col_arr.append((r,g,b))
    arr.append(col_arr)

# Put the 2D array into a df
rgb_codes = pd.DataFrame(arr)

# Set filename specified by user
filename = sys.argv[2] + ".xlsx"

# Use the XlsxWriter engine because this will help create square columns
writer = pd.ExcelWriter(filename, engine='xlsxwriter')

# Colour in the background of each cell, and then output to writer
rgb_codes.style.applymap(lambda v: f'background-color:#{"%02x%02x%02x" % v};').to_excel(writer,sheet_name="Sheet1",header=False,index=False)

# Set all cells to be square by making cols only 2 wide
for col in range(len(rgb_codes.columns)):
    writer.sheets["Sheet1"].set_column(col, col, 2)

# Save writer (therefore finalizing excel output)
writer.save()