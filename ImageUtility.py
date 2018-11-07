import numpy as np

########## PGM
def readPgm(name):
    with open(name, 'r') as f:
        lines = f.readlines()
        #Ignores commented lines
        for i in list(lines):
            if i[0] == '#':
                lines.remove(i)
    # Makes sure it is ASCII format (P2)
    assert lines[0].strip() == 'P2'

    # Converts data to a list of integers
    data = []
    for line in lines[1:]:
        for c in line.split():
            data.extend([int(c)]) 
    return np.array(data[3:]),(data[1], data[0], data[2])  #[image_data, (h,w,max)]

def writePgm(name, data):  #[image_data, (h,w,max)]
    h = data[1][0]
    w = data[1][1]

    with open(name, 'w') as f:
        f.write("P2\n")
        f.write("# Theia Debug\n")
        f.write(str(w) + " " + str(h)+ "\n")
        f.write(str(data[1][2]) + "\n")
        
        for i in range(w*h):
            f.write(str(data[0][i]) + " ") 
            if((i+1)%w == 0):
                f.write("\n") 
    return True 