#coding=UTF-8
import PIL
from PIL import Image
import numpy as np
from Tkinter import *
import Tkinter as tk


tk = Tk()

# name = './p2.pgm'
# def readpgm(name):
    # with open(name, 'r') as f:
        # lines = f.readlines()
        # #Ignores commented lines
        # for i in list(lines):
            # if i[0] == '#':
                # lines.remove(i)
    # # Makes sure it is ASCII format (P2)
    # assert lines[0].strip() == 'P2'

    # # Converts data to a list of integers
    # data = []
    # for line in lines[1:]:
        # data.extend([int(c) for c in line.split()]) 
    # return np.array(data[3:]),(data[0], data[1], data[2])
    

# data = readpgm(name)
# print data

# reshaped = np.reshape(data[0],(24, 7))

# plt.imshow(reshaped, cmap = plt.cm.gray)


# def writePgm(name, data):  #[image_data, (h,w,max)]
    # h = data[1][1]
    # w = data[1][0]

    # with open(name, 'w') as f:
        # f.write("P2\n")
        # f.write("# Shows\n")
        # f.write(str(w) + " " + str(h)+ "\n")
        # f.write(str(data[1][2]) + "\n")
        
        # for i in range(w*h):
            # f.write(str(data[0][i]) + " ") 
            # if((i+1)%w == 0):
                # f.write("\n") 
    # return True 

# writePgm("1.pgm",data)

img = PIL.Image.open(":/Desktop/1467100861-2794424496.png")
rushMore = ImageTk.PhtoImage(img)

canvas = Canvas(tk,width = img.size[0]+40,height = img.siz[1]+30)
canvas.create_image(20,15,anchor = NW, image = rushMore)
canvas.pack(fill = BOTH, expand = True)





