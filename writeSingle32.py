import time
import spidev
import SPIUtility
import ImageUtility

spi = None
data = [];
data_info = None;
def setUp():
    print("==> writeSingle32 setUp")
    global spi
    global data
    global data_info

    # spi setting
    # We only have SPI bus 0 available to us on the Pi
    bus = 0

    #Device is the chip select pin. Set to 0 or 1, depending on the connections
    device = 0

    # Enable SPI
    spi = spidev.SpiDev()

    # Open a connection to a specific bus and device (chip select pin)
    spi.open(bus, device)

    # Set SPI speed and mode
    spi.max_speed_hz = 100000
    spi.mode = 0

    #caculate bit error rate
    data_list = ImageUtility.readPgm("777.pgm")
    data = data_list[0]
    data_info = data_list[1]
    #data = [2,3,4,5,9,10,13,15]
    SPIUtility.resetDefaultAddress()

def runTest():
    global spi
    global data
    global data_info
    tx_data = SPIUtility.writeSingle32(0,data)
    ret = spi.xfer2(tx_data)
    # for i in range(len(data)):
        # tx_data = SPIUtility.writeSingle32(i,data[i])
        # ret = spi.xfer2(tx_data)
        
    # for i in range(len(data)):
        # tx_data = SPIUtility.writeSingle8(i,data)
        # tx_data.append(int(data[i]))
        # ret = spi.xfer2(tx_data)
        # print("tx_data:", tx_data)
    # print("tx_data:", tx_data)
    # return tx_data

    #### readSingle8
    print("==> writeSingle32 readSingle8")
    response = []
    for i in range(len(data)):
        rx_data = SPIUtility.readSingle8(i)
        ret = spi.xfer2(rx_data)
        response.append(ret[2])
        print(response[i])
    is_pass = True
    for i in range( len(response) ):
        if(data[i] != response[i]):
            print(i)
            print(data[i])
            print(response[i])
            is_pass = False
            print("Fail writeSingle32 readSingle8")
            break

    #### readBurst8
    print("==> writeSingle32 readBurst8")
    rx_data = SPIUtility.readBurst8(0,len(data))
    ret = spi.xfer2(rx_data)

    response = ret[2:]
    
    is_pass = True
    for i in range( len(response) ):
        if(data[i] != response[i]):
            is_pass = False
            print("Fail writeSingle32 readBurst8")
            break

    #### readSingle32
    print("==> writeSingle32 readSingle32")
    response = []
    for i in range(len(data)/4):
        rx_data = SPIUtility.readSingle32(i*4,4)
        ret = spi.xfer2(rx_data)
        for j in reversed(ret[5:]):
            response.append(j)
    #print(data)
    #print(response)

    is_pass = True
    for i in range( len(response) ):
        if(data[i] != response[i]):
            print(i)
            print(data[i])
            print(response[i])
            is_pass = False
            print("Fail writeSingle32 readSingle32")
            break
  
    #### readImage
    print("==> writeSingle32 readImage")
    response = []
    rx_data = SPIUtility.readImage(len(data)+1)
    ret = spi.xfer2(rx_data)
    rx_data = ret[2:]
    ImageUtility.writePgm("3.pgm",[rx_data, data_info])
    response = ret[2:]
    is_pass = True
    for i in range( len(response) ):
        if(data[i] != response[i]):
            is_pass = False
            print("Fail writeSingle32 readImage")
            break
    return is_pass

def tearDown():
    global spi
    spi.close()
