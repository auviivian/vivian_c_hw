import time
import spidev
import datetime
import numpy as np
import matplotlib.pyplot as plt
import glob as gb

# We only have SPI bus 0 available to us on the Pi
bus = 0

#Device is the chip select pin. Set to 0 or 1, depending on the connections
device = 0

# Enable SPI
spi = spidev.SpiDev()

# Open a connection to a specific bus and device (chip select pin)
spi.open(bus, device)

# Set SPI speed and mode
spi.max_speed_hz = 50000
spi.mode = 0

def readpgm(name):
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
        data.extend([int(c) for c in line.split()])
    return np.array(data[3:]),(data[1], data[0], data[2])

name_list = list()
img_path = gb.glob("./PGM/*")
print (img_path)
for filename in img_path:
    print ('filename:',filename)
    name_list.append(filename)

#caculate bit error rate
err = 0
repeat = 1000
image_length = 0
data = readpgm(name_list[0])
for i in range(repeat):
    print("count:", i)
    for i in range(repeat):
        print("count:", i)
        for name in name_list:
            #convert data to image_data_listlist
            image_data_list = list(data[0])
            print("image_data_list", list(data[0]))
            print("image_data_Length", len(image_data_list))
            length = len(image_data_list)
            image_length = length
            #combine opcode +address +image_data_listlist -> tx_data
            tx_data = [0x26,0x00]
            for i in range(length):
                tx_data.append(image_data_list[i])
            print("make tx_data", tx_data)

            #combine opcode +address +zero_padding -> tx_data
            rx_raw_data = [0x22,0x00]
            for i in range(length):
                rx_raw_data.append(0)
            print("make rx_raw_data", tx_data)

            #send tx_data
            spi.xfer2(tx_data)

            #read rx_raw_data
            ret = spi.xfer2(rx_raw_data)

            #parsing rx_raw_data ignore opcode and address
            rx_data = ret[2:]
            print("show rx_data", rx_data)

            #caculate bit error rate
            #err = 0
            for i in range(length):
                if rx_data[i] != image_data_list[i]:
                    err = err + 1
err_rate = float(err)/float(image_length*repeat)
print("err_rate:", err_rate)
print("repeat:", repeat)
#spi.close()
time.sleep(1)
