


def writePgm(name, data):  #[image_data, (h,w,max)]
    h = data[1][0]
    w = data[1][1]

    with open(name, 'w') as f:
        f.write("P2\n")
        f.write("# Shows\n")
        f.write(str(w) + " " + str(h)+ "\n")
        f.write(str(data[1][2]) + "\n")
        
        for i in range(w*h):
            f.write(str(data[0][i]) + " ") 
            if((i+1)%w == 0):
                f.write("\n") 
    return True  


writePgm(output_filename , [rx_data , data[1]] )
